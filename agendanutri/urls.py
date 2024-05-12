from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendanutri/cadastrar/', views.cadastrar, name='cadastro_pacientes'),
    path('agendanutri/cadastradocomsucesso/', views.sucesso_cadastro, name='sucesso_cadastro'),
    path('agendanutri/listadepacientes/', views.exibir_lista_pacientes, name='lista_pacientes'),
    path('agendanutri/marcar/', views.marcar_consulta, name='marcar_consulta'),
    path('agendanutri/agendamentos/', views.lista_consultas, name='lista_consultas'),
]
