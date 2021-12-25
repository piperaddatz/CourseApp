from django.urls import path
from .views import views

app_name='Appunte'

urlpatterns = [
        # INICIO
        path(r'', views.index, name="index")
]