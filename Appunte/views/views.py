from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from ..forms import RegistrationForm
from ..models import Course

User = get_user_model()


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


###############    Views de Usuarios

def perfil_usuario(request):
    return render(request, 'index.html', {})


def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'registration/register.html', {})


###########################     Views of Courses     #######################

def coursesList(request):
    courses = Course.objects.all()
    # if not request.user.is_authenticated:
    #    return redirect('/accounts/login/')

    return render(request, 'courses/list.html', {"courses": courses})


def palmera(request):
    return render(request, 'palmera.html', {})
