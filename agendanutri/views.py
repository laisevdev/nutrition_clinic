from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendaForm, PacienteForm
from .models import Agenda, Paciente


def index(request):
    return render(request, 'agendanutri/index.html', {})

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

def exibir_lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'agendanutri/lista_pacientes.html', {'pacientes': pacientes})

def dados_paciente(request, pk):
    dados_do_paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'agendanutri/dados_paciente.html', {'dados_do_paciente': dados_do_paciente})

def editar_pacientes(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.author = request.user
            paciente.save()
            return redirect('dados_paciente', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'agendanutri/editar_pacientes.html', {'form': form}) 

def deletar_pacientes(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        paciente.delete()
        return redirect('sucesso_exclusao',)
    else:
        return render(request, 'agendanutri/paciente_deletado.html', {}) 

def sucesso_exclusao(request):
    return render(request, 'agendanutri/sucesso_exclusao.html', {})

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