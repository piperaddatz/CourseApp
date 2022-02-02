from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Course


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'rol')


class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        label='Nombre de Usuario',
        max_length=30,
    )

    email = forms.EmailField(
        label='Correo',
    )

    password = forms.CharField(
        label='Contraseña',
    )

    def clean_username(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data['username']
        if User.users.filter(username=username):
            self.add_error(
                'username',
                forms.ValidationError("User Exists")
            )

        return username

    def clean_email(self):
        cleaned_data = super(RegistrationForm, self).clean()
        email = cleaned_data['email']
        if User.users.filter(email=email):
            self.add_error(
                'email',
                forms.ValidationError(
                    "Mail exists")
            )

        return email

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

    def save(self):
        cleaned_data = super(RegistrationForm, self).clean()

        user_data = {
            'email': cleaned_data['email'],
            'username': cleaned_data['username'],
        }
        user = User(**user_data)
        user.set_password(cleaned_data['password'])
        user.save()

        return user


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'teacher', 'price', 'is_published', 'picture')
