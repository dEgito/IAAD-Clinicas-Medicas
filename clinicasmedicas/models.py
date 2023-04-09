from django.db import models

# Create your models here.
class Clinica(models.Model):
    CodCli = models.CharField(max_length=7, primary_key=True)
    NomeCli = models.CharField(max_length=40)
    Endereco = models.CharField(max_length=40, null=True, blank=True)
    Telefone = models.CharField(max_length=16, null=True, blank=True)
    Email = models.CharField(max_length=40, null=True, blank=True)

class Especialidade(models.Model):
    CodEspec = models.CharField(max_length=7, primary_key=True)
    NomeEspec = models.CharField(max_length=25)
    Descricao = models.TextField()

class Medico(models.Model):
    CodMed = models.CharField(max_length=7, primary_key=True)
    NomeMed = models.CharField(max_length=40)
    Genero = models.CharField(max_length=40, null=True, blank=True)
    Telefone = models.CharField(max_length=16, null=True, blank=True)
    Email = models.CharField(max_length=40, unique=True)
    CodEspec = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

class ClinicaMedico(models.Model):
    CodCli = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    CodMed = models.ForeignKey(Medico, on_delete=models.CASCADE)
    DataIngresso = models.DateField()
    CargaHorariaSemanal = models.DecimalField(max_digits=3, decimal_places=1, default=20.0)
    class Meta:
        unique_together = ('CodCli', 'CodMed')