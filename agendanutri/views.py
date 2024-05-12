from django.shortcuts import render, redirect
from .forms import AgendaForm, PacienteForm
from .models import Agenda
from .models import Paciente
from django.utils import timezone

def index(request):
    return render(request, 'agendanutri/index.html', {})

def exibir_lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'agendanutri/lista_pacientes.html', {'pacientes': pacientes})

def cadastrar(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('sucesso_cadastro',)
    else:
        form = PacienteForm()
    return render(request, 'agendanutri/cadastro_pacientes.html', {'form': form})
    
def sucesso_cadastro(request):
    return render(request, 'agendanutri/sucesso_cadastro.html', {})

def marcar_consulta(request):        
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            paciente_id = request.POST.get('id_paciente')
            post.id_paciente_id = paciente_id
            post.save()
            return redirect('lista_consultas',)
    else:
        form = AgendaForm()
    return render(request, 'agendanutri/marcar_consulta.html', {'form': form})        
    
def lista_consultas(request):
    consultas = Agenda.objects.all()
    return render(request, 'agendanutri/lista_consultas.html',  {'consultas': consultas})