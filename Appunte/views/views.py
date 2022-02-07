from django.shortcuts import render, redirect
from django import forms
from ..forms import CourseForm, CustomUserCreationForm, RegistrationForm
from ..models import Course, Topic, Subtopic, Question, Answer
from ..managers import CustomUserManager

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'index.html', {})



###############    Views de Usuarios

def PerfilUsuario(request):
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
            return redirect('../../cursos/lista')
    
    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'registration/register.html', {}) 





###########################     Views of Courses     #######################

def coursesList(request):
    courses = Course.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    return render(request, 'courses/list.html', {"courses":courses})


def palmera(request):
        
    return render(request, 'palmera.html', {})    



###########################     Views of Topics     #######################

def topicList(request, pk):
    topics = Topic.objects.filter(course=pk)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    return render(request, 'topic/list.html', {"topics":topics})




 
def subtopicList(request, pk):
    subtopics = Subtopic.objects.filter(topic=pk)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    return render(request, 'subtopic/list.html', {"subtopics":subtopics})   



def showQuestion(request, pk):
    questions = Question.objects.filter(subtopic=pk)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    return render(request, 'question/show.html', {"questions":questions} )       



def showAnswer(request, pk):
    answer = Answer.objects.filter(question=pk)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

   # return render(request, 'question/list.html', {"answers":answers})     