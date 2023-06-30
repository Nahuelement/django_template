

from django.urls import path
from app1 import views
from .views import Plato

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.eventos_congresos, name='eventos_congresos'),
    path('platos/', Plato, name='plato'),
]