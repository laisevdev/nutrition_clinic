from django import forms
from .models import Agenda, Paciente


class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ('data_consulta', 'id_paciente',)
        widgets = {
            'data_consulta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'cpf', 'endereco', 'sexo', 'idade', 'peso', 'altura',)
        

