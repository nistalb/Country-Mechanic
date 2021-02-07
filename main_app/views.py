from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProfileForm, EquipmentForm

# import models
from .models import User, Profile, Equipment, Task, Tool, Consumables, Maint_Record 

# Create your views here.
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
                return rendter(request, 'home.html', context)
            else:
                if signup_form.is_valid():
                    user = signup_form.save()
                    login(request, user)
                    return redirect('main/')
                else:
                    context = {'error': 'Invalid signup, please try again'}
                    return render(request, 'home.html', context)

    signup_form = NewUserForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form}
    return render(request, 'home.html', context)

def main(request):

    if Equipment.objects.filter(user_id=request.user.id):
        equipment = Equipment.objects.filter(user_id=request.user.id)
    else:
        equipment = ""
    context = {'equipment': equipment}
    return render(request, 'main.html', context)

def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    user = User.objects.get(id=request.user.id)
    if Profile.objects.filter(user_id=request.user.id):
        profile = Profile.objects.get(user_id=request.user.id)
    else:
        profile = ""
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

def equipment_create(request):
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment = equipment_form.save(commit=False)
            equipment.user = request.user
            equipment.save()
            return redirect('main')

    
    equipment_form = EquipmentForm()
    context = {'equipment_form': equipment_form}
    return render(request, 'equipment/create.html', context)

def equipment_show(request, equipment_id):

    if Equipment.objects.filter(user_id=request.user.id):
        equipment_all = Equipment.objects.filter(user_id=request.user.id)
    else:
        equipment_all = ""
    equipment_id = Equipment.objects.get(id=equipment_id)
    context = {'equipment_all': equipment_all, 'equipment_id': equipment_id}
    return render(request, 'equipment/show.html', context)

def equipment_delete(request, equipment_id):
    Equipment.objects.get(id=equipment_id).delete()
    return redirect('main')
