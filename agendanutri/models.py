from django.db import models
from django.utils import timezone


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    idade = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)  
    altura = models.DecimalField(max_digits=3, decimal_places=2)  

    def __str__(self):
        return self.nome
  
class Agenda(models.Model):
    data_consulta = models.DateTimeField()
    data_retorno = models.DateTimeField(auto_now = False, auto_now_add = False, null=True, blank=True)
    data_reagendamento = models.DateTimeField(auto_now = False, auto_now_add = False, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now = False, auto_now_add = False, default=timezone.now())
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def criacao(self):
        self.data_criacao = timezone.now()
        self.save()