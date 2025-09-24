from django.db import models
import uuid
import random
from django.utils import timezone


def obtener_numero_random():
    random_nro = random.randint(10000, 99999)
    for i in range(5):
        if not Curso.objects.filter(numero_curso=random_nro).exists():
            return random_nro
        random_nro = random.randint(10000, 99999)
    raise Exception("Se intento crear un curso con numeros ya existentes.")


class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    numero_curso = models.IntegerField(default=obtener_numero_random, unique=True)
    fecha_creacion = models.DateField(default=timezone.now)
    code = models.CharField(
        unique=True,
        editable=False,
        default=uuid.uuid4,  # bkajsghdba-jlakhflaf-qlheqwklj-lhjflajnf
        max_length=32
    )
    # enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nro de Curso: {self.numero_curso}"
