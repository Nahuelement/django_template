

from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.eventos_congresos, name='eventos_congresos'),
]