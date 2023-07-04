from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    img = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre_plato

class Comentarios(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    opinion = models.TextField(max_length=200)
    nota = models.IntegerField()
    def __str__(self):
        return self.nombre_cliente


class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    email = models.EmailField()
    personas = models.IntegerField()
    comentarios = models.TextField(max_length=200)
    def __str__(self):
        return f'{self.nombre } {self.apellido }'