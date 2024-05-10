from django.shortcuts import render

def index(request):
    return render(request, 'agendanutri/index.html', {})

def marcar_consulta(request):
    return render (request, 'agendanutri/marcar_consulta.html', {})