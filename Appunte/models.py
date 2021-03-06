from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# USUARIO CUSTOM
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=264)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    rol = models.CharField(max_length=12,default="student")
    profile_pic = models.ImageField(upload_to='user_profile',blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



# CURSO
class Course(models.Model):
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=5000) 
    teacher =  models.CharField(max_length=100) 
    is_pay = models.BooleanField(default=False)
    price = models.CharField(max_length=15)
    published = models.BooleanField(default=False)
    course_pic = models.ImageField(upload_to='course_profile',blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name


# Topic
class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    name = models.CharField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name        


# Subtopic
class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    name = models.CharField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name   


class Question(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE) 
    sort = models.IntegerField()
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.content   


class Answer(models.Model):
    answer = models.ForeignKey(Question, on_delete=models.CASCADE) 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.content                      