from django.urls import path
from .views import views

app_name='Appunte'

urlpatterns = [
        # INICIO
        path(r'', views.index, name="index"),

     
        # PERFIL
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/salir/', views.salir, name='salir'),

        # COURSE 
        path('cursos/lista', views.coursesList, name="course-list"),

        # TOPIC 
        path('cursos/lista/<int:pk>', views.topicList, name="topic-list"),
        path('cursos/lista/subtopic/<int:pk>', views.subtopicList, name="subtopic-list"),

        # Question 
        path('cursos/pregunta/<int:pk>', views.showQuestion, name="question-show"),
]