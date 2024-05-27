from django import forms
from .models import Agenda, Paciente


class AgendaForm(forms.ModelForm):

    HORARIOS_DISPONIVEIS = [
        ("08:00", "08:00"),
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
    ]
    
    horario_consulta = forms.ChoiceField(choices=HORARIOS_DISPONIVEIS, label="Horário")

    class Meta:
        model = Agenda
        fields = ('data_consulta', 'id_paciente',)
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
        }

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'cpf', 'endereco', 'sexo', 'idade', 'peso', 'altura',)
        

