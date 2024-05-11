from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendanutri/marcar/', views.marcar_consulta, name='marcar_consulta'),
    path('agendanutri/agendamentos/', views.lista_consultas, name='lista_consultas'),
]
