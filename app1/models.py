from django.db import models

# Create your models here.

class Name(models.Model):
    primer_nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return

