from django.shortcuts import render
# from .models import Estudiante # Relativa
from core.models import Estudiante # Absoluta
# Create your views here.
# dict.items() -> dict_items([(k1, v1), (k2, v2), ...])
def hola_mundo(request):
    return render(request, "core/hola.html")

def estudiante_list(request):
    # Lógica para obtener la lista de estudiantes desde la base de datos
    estudiantes = Estudiante.objects.all() # QuerySet([<Estudiante>, <Estudiante>, ...])
    #estudiantes = Estudiante.objects.filter(nombre__startswith="F") # QuerySet([<Estudiante>, <Estudiante>, ...])
    contexto = {
        "lista_estudiantes": estudiantes
    }
    return render(request, "core/estudiantes_list.html", contexto)
