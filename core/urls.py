from django.urls import path
from .views import hola_mundo, estudiante_list

urlpatterns = [
    path("", hola_mundo, name="hola"),
    path("listar-estudiantes/", estudiante_list, name="listar-estudiantes"),
]
