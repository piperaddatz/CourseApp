from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . import models
from .models import CustomUser, Course



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')

    def save(self, commit=True):
        CustomUser = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()
        return CustomUser    



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'teacher', 'is_pay', 'price', 'published', 'course_pic' )          