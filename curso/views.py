from django.shortcuts import render
from django.urls import reverse_lazy
from curso.models import Curso
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class CursoListView(ListView):
    model = Curso
    template_name = "curso/curso_list.html"
    context_object_name = "lista_curso"

    def get_queryset(self):
        return Curso.objects.filter(numero_curso__gt=15000)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listado de cursos"
        context['titulo_tabla'] = "Cursoss disponibles"
        return context

class CursoDetailView(DetailView):
    model = Curso
    template_name = "curso/curso_detail.html"
    context_object_name = "curso"
    slug_field = "code"
    slug_url_kwarg = "code"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "curso/curso_form.html"
    fields = ["nombre"]
    success_url = reverse_lazy("curso:listar-cursos")


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "curso/curso_confirm_delete.html"
    slug_field = "code"
    slug_url_kwarg = "code"
    success_url = reverse_lazy("curso:listar-cursos")


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "curso/curso_form.html"
    fields = ["nombre", "numero_curso"]
    slug_field = "code"
    slug_url_kwarg = "code"
    success_url = reverse_lazy("curso:listar-cursos")
