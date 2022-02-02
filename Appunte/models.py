from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

import uuid

from Appunte.managers import UserManager

# Cambios generales
#   - Orden
#   - Eliminados traductores


ROL_STUDENT = "STUDENT"
ROL_TEACHER = "TEACHER"
ROL_STAFF = "STAFF"

# Camabios Usuario:
#   - Nombre remplazado para mayor claridad
#   - Eliminar traductor en para el campo 'email'
#   - Eliminar el campo 'is_staff', redundante con 'rol'
#   - Renombado el campo 'date_joined' a 'created_at'
#   - Renombrado 'profile_pic' a 'picture', y su carpeta de subida
#   - Eliminado el campo REQUIRED_FIELDS ya que esta implementado en la clase herdada
#   - Cambio de 'rol' de campo de texto a un int pequeño y creadas constantes de rol
#   - Usar auto_now_add=True en lugar de datetime.now en 'created_at'
#   - Renombrado manager. 'objects' es el nombre por defecto, pero el plural de la clase debe ser preferido

# Usuario TODO Documentar
class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    users = UserManager()

    email = models.EmailField('email', unique=True)
    username = models.CharField(max_length=264)

    is_active = models.BooleanField(default=True)  # TODO? Override, puede llevar a problemas

    rol = models.CharField(max_length=10, default=ROL_STUDENT)
    picture = models.ImageField(upload_to='users/profiles', blank=True)

    # ref: https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
    USERNAME_FIELD = 'uuid'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

# Camabios Curso:
#   - Agregado UUID
#   - Cambiar el tipo de campo de 'teacher' de texto a un ForeignKey de User
#   - Cambiar el tipo de campo de 'price' de texto a int
#   - Eliminado 'is_payed'. Usar price==0
#   - Renombrado 'course_pic' a 'picture', y su carpeta de subida
#   - Renombrado 'published' a 'is_published'


# Curso TODO Documentar
class Course(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='courses/profiles', blank=True)

    def __str__(self):
        return self.name
