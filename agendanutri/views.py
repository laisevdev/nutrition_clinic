from django.shortcuts import render, redirect
from .forms import AgendaForm
from .models import Agenda

def index(request):
    return render(request, 'agendanutri/index.html', {})

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