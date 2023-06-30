from django.shortcuts import render
from django.http import HttpResponse
from .models import Plato

def home(request):
    platos = Plato.objects.all()
    return render(request, "home.html", {"platos":platos})

def eventos_congresos(request):
    return render(request, 'eventos_congresos.html')
# Create your views here.
