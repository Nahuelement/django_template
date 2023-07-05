from django.contrib import admin
from .models import Plato, Comentarios, Reservas, Evento

# Register your models here.

admin.site.register(Plato)
admin.site.register(Comentarios)
admin.site.register(Reservas)
admin.site.register(Evento)

