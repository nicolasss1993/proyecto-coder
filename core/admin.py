from django.contrib import admin
from core.models import Estudiante
# Register your models here.

# admin.site.register(Estudiante)


@admin.register(Estudiante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nro_legajo", "email", "fecha_creacion")
    search_fields = ("nombre",)
    list_filter = ("fecha_creacion",)
    ordering = ("apellido", "nombre")
    list_per_page = 10
