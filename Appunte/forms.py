from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from . import models
from .models import CustomUser, Course



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'rol')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'teacher', 'is_pay', 'price', 'published', 'course_pic' )          