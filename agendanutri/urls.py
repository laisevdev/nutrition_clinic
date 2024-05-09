from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('', views.lista_agendamentos, name='lista_agendamentos'),
]
