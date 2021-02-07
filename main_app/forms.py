from django.forms import ModelForm
from .models import Profile, User, Equipment, Task

from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'hourly_rate')

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ('model', 'make', 'mfg_year', 'description', 'mileage', 'hours', 'img_url', 'cost')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =('task_name', 'description', 'interval', 'duration', 'instructions', 'video')

