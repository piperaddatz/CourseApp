from django.contrib import admin
import django.contrib.auth.admin

from . import models
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    model = User

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('email', 'username', 'rol', 'picture', 'is_active', 'created_at')
    list_filter = ('email', 'username', 'rol', 'is_active',)
    fieldsets = (
        ('General', {'fields': ('email', 'username', 'password', 'picture')}),
        ('Permissions', {'fields': ('rol', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'rol', 'picture', 'password1', 'password2', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(models.Course)
