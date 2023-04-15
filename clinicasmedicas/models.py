from django.db import models

class Clinica(models.Model):
    cod_cli = models.CharField(primary_key=True, max_length=7)
    nome_cli = models.CharField(max_length=40)
    endereco = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

class Especialidade(models.Model):
    cod_espec = models.CharField(primary_key=True, max_length=7)
    nome_espec = models.CharField(max_length=25)
    descricao = models.TextField()

class Medico(models.Model):
    cod_med = models.CharField(primary_key=True, max_length=7)
    nome_med = models.CharField(max_length=40)
    genero = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=40, unique=True)
    cod_espec = models.ForeignKey(Especialidade, on_delete=models.CASCADE)



class ClinicaMedico(models.Model):
    cod_cli = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    cod_med = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_ingresso = models.DateField()
    carga_horaria_semanal = models.DecimalField(max_digits=3, decimal_places=1, default=20.0)
    class Meta:
        unique_together = ('cod_cli', 'cod_med')