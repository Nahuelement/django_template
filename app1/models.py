from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    img = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

