from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

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
    return render(request, 'main.html')