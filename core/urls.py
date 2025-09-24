from django.urls import path
from .views import hola_mundo, estudiante_list, crear_estudiante, editar_estudiante, eliminar_estudiante, estudiante_detail

urlpatterns = [
    path("", hola_mundo, name="hola"),
    path("listar-estudiantes/", estudiante_list, name="listar-estudiantes"),
    path("crear-estudiante-model", crear_estudiante, name="crear-estudiante-model"),
    path("editar-estudiante/<int:pk>/", editar_estudiante, name="editar-estudiante"),
    path("eliminar-estudiante/<int:pk>/", eliminar_estudiante, name="eliminar-estudiante"),
    path("estudiante-detalle/<int:pk>/", estudiante_detail, name="detalle-estudiante")
]
