from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from . import models
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'rol')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol')