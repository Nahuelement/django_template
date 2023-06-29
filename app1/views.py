from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "base.html")

def eventos_congresos(request):
    return render(request, 'eventos_congresos.html')
# Create your views here.
