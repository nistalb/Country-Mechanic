from django.forms import ModelForm
from .models import Profile, User, Equipment, Task, Tool, Consumables, Photo

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
        fields = ('model', 'make', 'mfg_year', 'description', 'mileage', 'hours', 'cost')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =('task_name', 'description', 'interval', 'duration', 'instructions', 'video')

class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = ('tool_name', 'description')

class ConsumableForm(ModelForm):
    class Meta:
        model = Consumables
        fields = ('name', 'description', 'part_number', 'source', 'cost')

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('url',)