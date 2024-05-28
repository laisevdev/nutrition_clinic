from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendaForm, PacienteForm
from .models import Agenda, Paciente
from django.contrib import messages
from datetime import datetime


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
    try:
        if request.method == "POST":
            form = AgendaForm(request.POST)
            if form.is_valid():
                paciente_id = form.cleaned_data['id_paciente']
                data_consulta = form.cleaned_data['data_consulta']
                horario_consulta_str = form.cleaned_data['horario_consulta']
                horario_consulta = datetime.strptime(horario_consulta_str, "%H:%M").time()

                consultas = Agenda.objects.filter(data_consulta=data_consulta, horario_consulta=horario_consulta)
                if consultas.exists():
                    messages.error(request, "Já existe uma consulta marcada neste mesmo dia e horário. Por favor, escolha outra data.")
                else:
                    post = form.save(commit=False)
                    post.id_paciente = paciente_id
                    post.data_consulta = data_consulta
                    post.horario_consulta = horario_consulta
                    post.save()
                    return redirect('lista_consultas')
            else:
                messages.error(request, "O formulário contém erros. Por favor, corrija-os e tente novamente.")    
        else:
            form = AgendaForm()
    except Exception as e:
        messages.error(request, f"Ocorreu um erro inesperado: {str(e)}")

    return render(request, 'agendanutri/marcar_consulta.html', {'form': form})
    
    
def lista_consultas(request):
    consultas = Agenda.objects.all()
    return render(request, 'agendanutri/lista_consultas.html',  {'consultas': consultas})


    