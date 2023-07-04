from django.shortcuts import render
from django.http import HttpResponse
from .models import Plato, Reservas
from .forms import FormReservas

def home(request):
    platos = Plato.objects.all()
    return render(request, "home.html", {"platos":platos})

def eventos_congresos(request):
    return render(request, 'eventos_congresos.html')
# Create your views here.

def reservas(request):

    sent = False
    if request.method == 'POST':
        reserva = FormReservas(request.POST or None)
        if reserva.is_valid():
            sent = True
            cd = reserva.cleaned_data
            reserva_ok = Reservas.objects.create(**cd)
            return render(request, 'reservas.html',{'reserva':reserva_ok, 'sent':sent,'cd':cd})
    else:
        reserva = FormReservas()


    return render(request, 'reservas.html',{'reserva':reserva, 'sent':sent})
