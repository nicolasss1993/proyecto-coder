from django.urls import path
from curso.views import *

urlpatterns = [
    path("", CursoListView.as_view(), name="listar-cursos"),
    path("crear/", CursoCreateView.as_view(), name="crear-curso"),
    path("<str:code>/", CursoDetailView.as_view(), name="detalle-curso"),
    path("<str:code>/editar/", CursoUpdateView.as_view(), name="editar-curso"),
    path("<str:code>/eliminar/", CursoDeleteView.as_view(), name="eliminar-curso"),
]