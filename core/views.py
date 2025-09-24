from django.shortcuts import render, redirect, get_object_or_404
# from .models import Estudiante # Relativa
from core.models import Estudiante # Absoluta
from core.forms import EstudianteForm, EstudianteFormManual
# Create your views here.
# dict.items() -> dict_items([(k1, v1), (k2, v2), ...])
def hola_mundo(request):
    return render(request, "core/index.html")

# def estudiante_list(request):
#     # Lógica para obtener la lista de estudiantes desde la base de datos
#     estudiantes = Estudiante.objects.all() # QuerySet([<Estudiante>, <Estudiante>, ...])
#     #estudiantes = Estudiante.objects.filter(nombre__startswith="F") # QuerySet([<Estudiante>, <Estudiante>, ...])
#     # Estudiante.objects.filter(nombre__startswith="A", edad__gte=15) # AND
#     contexto = {
#         "lista_estudiantes": estudiantes
#     }
#     return render(request, "core/estudiantes_list.html", contexto)

# POST - Crear info / GET - Pedir info / DELETE = Eliminar / PUT,UPDATE = Editar
def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("listar-estudiantes")
    else:
        formulario = EstudianteForm()

    return render(request, "core/estudiante_form.html", {"form": formulario})


def estudiante_list(request):
    query = request.GET.get("q", "")
    
    if query:
        lista_estudiantes = Estudiante.objects.filter(nombre__icontains=query)
    else:
        lista_estudiantes = Estudiante.objects.all()
    
    contexto = {
        "lista_estudiantes": lista_estudiantes
    }
    return render(request, "core/estudiantes_list.html", contexto)


def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("listar-estudiantes")
    else:
        form = EstudianteForm(instance=estudiante)

    return render(request, "core/estudiante_form.html", {"form": form})


def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        return redirect("listar-estudiantes")
    return redirect("listar-estudiantes")


def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    contexto = {
        "estudiante": estudiante
    }
    return render(request, "core/estudiante_detail.html", {"estudiante": estudiante})
