from django import template
from ..models import Plato
from django.db import models
from django.db.models import F
from django.db.models.functions import Cast

register = template.Library()

@register.simple_tag
def get_ofertas():

    platos_promocion = Plato.objects.all()
    platos_promocion = platos_promocion.annotate(promocion=Cast( F('precio')*0.8, models.IntegerField()) )


    return platos_promocion