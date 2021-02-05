from django.forms import ModelForm
from .models import Profile, User

from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')