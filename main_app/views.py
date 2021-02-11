from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProfileForm, EquipmentForm, TaskForm, ToolForm, ConsumableForm, PhotoForm

# import models
from .models import User, Profile, Equipment, Task, Tool, Consumables, Maint_Record, Photo

# AWS Imports
import boto3
import uuid

# AWS Constants
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'country-mechanic'


# ==== Home ====
def home(request):
    if request.method == 'POST':
        signup_form = NewUserForm(request.POST)
        username_form = request.POST['username']
        email_form = request.POST['email']
        if User.objects.filter(username=username_form).exists():
            context={'error': 'Username is already taken'}
            return render(request, 'home.html', context)
        else:
            if User.objects.filter(email=email_form).exists():
                context={'error': 'Email is already taken'}
                return render(request, 'home.html', context)
            else:
                if signup_form.is_valid():
                    user = signup_form.save()
                    login(request, user)
                    return redirect('garage/')
                else:
                    context = {'error': 'Invalid signup, please try again'}
                    return render(request, 'home.html', context)

    signup_form = NewUserForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form}
    return render(request, 'home.html', context)

# === Garage ====
def garage(request):
    equipment = Equipment.objects.filter(user_id=request.user.id)
    context = {'equipment': equipment}
    return render(request, 'garage.html', context)

# === Profile ===
def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect('profile')

    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    profile_form = ProfileForm()
    context = {'user': user, 'profile_form': profile_form, 'profile': profile}
    return render(request, 'profile/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user_id=request.user.id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        location = request.POST['location']
        hourly_rate = request.POST['hourly_rate']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            context={'error': 'Username is already taken'}
            return render(request, 'profile/edit.html', context)
        else:
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                context={'error': 'Email is already taken'}
                return render(request, 'profile/edit.html', context)
            else:

                user.last_name = last_name
                user.first_name = first_name
                user.email = email
                user.profile.location = location
                user.profile.hourly_rate = hourly_rate
                user.save()
                return redirect('profile')

    profile_form = ProfileForm(instance=profile)
    user_form = NewUserForm(instance=user)
    context = {'profile_form': profile_form, 'user_form': user_form, 'user': user, 'profile': profile}
    return render(request, 'profile/edit.html', context)

def profile_delete(request):
    User.objects.get(id=request.user.id).delete()
    return redirect('home')


# === Equipment ===
def equipment_create(request):
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment = equipment_form.save(commit=False)
            equipment.user = request.user
            equipment.save()
            return redirect('equipment_show', equipment_id=equipment.id)

    equipment_form = EquipmentForm()
    context = {'equipment_form': equipment_form}
    return render(request, 'equipment/create.html', context)

def equipment_show(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    tasks = equipment.task_set.all()
    task_ids = tasks.values_list('id')
    maintenance = equipment.maint_record_set.all()
    tools = Tool.objects.filter(task__in = task_ids).distinct()
    consumables = Consumables.objects.filter(task__in = task_ids).distinct()
    context = {'equipment': equipment, 'tasks': tasks, 'maintenance': maintenance, 'tools': tools, 'consumables': consumables}
    return render(request, 'equipment/show.html', context)

def equipment_edit(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST, instance=equipment)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect( 'equipment_show', equipment_id=equipment.id)

    equipment_form = EquipmentForm()
    context = {'equipment_form': equipment_form, 'equipment': equipment}
    return render(request, 'equipment/edit.html', context)

def equipment_delete(request, equipment_id):
    Equipment.objects.get(id=equipment_id).delete()
    return redirect('garage')

# === Task ====
def task_create(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.equipment = equipment
            task.save()
            return redirect('task_edit', task_id=task.id)
    
    task_form = TaskForm()
    context = {'task_form': task_form, 'equipment_id': equipment_id}
    return render(request, 'task/create.html', context)

def task_show(request, task_id):
    task = Task.objects.get(id=task_id)
    #available_tools = Tool.objects.filter(user_id=request.user.id).exclude(id__in = task.tool.all().values_list('id'))
    available_consumables = Consumables.objects.filter(user_id=request.user.id).exclude(id__in = task.consumable.all().values_list('id'))
    context = {'task': task, 'available_consumables': available_consumables}
    return render(request, 'task/show.html', context)

def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_show', task_id)

    available_consumables = Consumables.objects.filter(user_id=request.user.id).exclude(id__in = task.consumable.all().values_list('id'))
    available_tools = Tool.objects.filter(user_id=request.user.id).exclude(id__in = task.tool.all().values_list('id'))
    task_form = TaskForm()
    context = {'task_form': task_form, 'task': task, 'available_tools': available_tools, 'available_consumables': available_consumables}
    return render(request, 'task/edit.html', context)

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('equipment_show', equipment_id=task.equipment_id)

# === Maint Record ===
def create_maint_record(request, equipment_id, task_id):
    equipment = Equipment.objects.get(id=equipment_id)
    task = Task.objects.get(id=task_id)
    mileage = equipment.mileage
    hours = equipment.hours
    maint_record = Maint_Record.objects.create(mileage=mileage, hours=hours, task=task, equipment=equipment)
    maint_record.save()
    return redirect('equipment_show', equipment_id=equipment_id)

# === Tools ===
def tool_index(request):
    tools = Tool.objects.filter(user_id=request.user.id)
    context = {'tools': tools}
    return render(request, 'tool/index.html', context)

def tool_create(request):
    if request.method == 'POST':
        tool_form = ToolForm(request.POST)
        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            tool.user = request.user
            tool.save()
            return redirect('tool_index')

    tool_form = ToolForm()
    context = {'tool_form': tool_form}
    return render(request, 'tool/create.html', context)

def tool_delete(request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    tool.delete()
    return redirect('tool_index')

def tool_assoc(request, task_id, tool_id):
    Task.objects.get(id=task_id).tool.add(tool_id)
    return redirect('task_edit', task_id=task_id)

def tool_deassoc(request, task_id, tool_id):
    Task.objects.get(id=task_id).tool.remove(tool_id)
    return redirect('task_edit', task_id=task_id)

# === Consumables ===
def consumable_index(request):
    consumables = Consumables.objects.filter(user_id=request.user.id)
    context = {'consumables': consumables}
    return render(request, 'consumables/index.html', context)

def consumable_create(request):
    if request.method == 'POST':
        consumable_form = ConsumableForm(request.POST)
        if consumable_form.is_valid():
            consumable = consumable_form.save(commit=False)
            consumable.user = request.user
            consumable.save()
            return redirect('consumable_index')

    consumable_form = ConsumableForm()
    context = {'consumable_form': consumable_form}
    return render(request, 'consumables/create.html', context)

def consumable_delete(request, consumable_id):
    consumable = Consumables.objects.get(id=consumable_id)
    consumable.delete()
    return redirect('consumable_index')

def consumable_assoc(request, task_id, consumable_id):
    Task.objects.get(id=task_id).consumable.add(consumable_id)
    return redirect('task_edit', task_id=task_id)

def consumable_deassoc(request, task_id, consumable_id):
    Task.objects.get(id=task_id).consumable.remove(consumable_id)
    return redirect('task_edit', task_id=task_id)

# === Photo ===
def add_photo(request, equipment_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, equipment_id=equipment_id, user_id=request.user.id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('equipment_show', equipment_id=equipment_id)

def delete_photo(request, photo_id, equipment_id):
    Photo.objects.get(id=photo_id).delete()
    return redirect('equipment_show', equipment_id=equipment_id)
