from django.db import models


class Edificio(models.Model):
    capacidad = models.PositiveIntegerField(help_text="Capacidad de aforo del edificio")
    nombre = models.CharField(max_length=200)


class Persona(models.Model):
    rut = models.CharField(max_length=9, 
        help_text="Sin puntos ni guiones y con dígito verificador.",
        unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField(help_text="Sin código de país y con 9")
    es_menor = models.BooleanField(help_text="Indica si es un menor de edad")


class Evento(models.Model):
    fecha = models.DateTimeField()
    duracion = models.PositiveIntegerField(help_text="Cantidad de horas de duración del evento.")
    edificio = models.ForeignKey("Edificio", on_delete=models.CASCADE)


class Inscripcion(models.Model):
    persona = models.ForeignKey("Persona", on_delete=models.CASCADE)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE)


