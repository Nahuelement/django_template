from django.shortcuts import render
from django.http import HttpResponse

def vista(request):
    return HttpResponse("Hola mundo.")

# Create your views here.
