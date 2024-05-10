from django import forms
from .models import Agenda

class PostForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ('id_paciente', 'data_consulta', 'data_criacao',)