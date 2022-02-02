from django.urls import path

from .views import views

# Endpoints
urlpatterns = [
    # Index
    path('', views.index, name="index"),

    # Perfil
    path('accounts/profile/', views.perfil_usuario, name='perfil'),
    path('accounts/salir/', views.salir, name='salir'),

    # Cursos
    path('cursos/lista', views.coursesList, name="course-list"),
]
