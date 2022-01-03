from django.shortcuts import render, redirect
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'index.html', {})





###############    Views de Usuarios

def PerfilUsuario(request):
    return render(request, 'courses/list.html', {})

def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')    
