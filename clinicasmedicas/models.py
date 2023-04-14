from django.db import models

class EnderecoClinica(models.Model):
    cod_end_clinica = models.CharField(primary_key=True, max_length=7)
    rua_cli = models.CharField(max_length=20)
    bairro_cli = models.CharField(max_length=20)
    cep_cli = models.CharField(max_length=9)
    numero_end_cli = models.CharField(max_length=6)

class Clinica(models.Model):
    cod_cli = models.CharField(primary_key=True, max_length=7)
    cod_end_clinica = models.ForeignKey(EnderecoClinica, on_delete=models.CASCADE)

class NomeClinica(models.Model):
    cod_cli = models.OneToOneField(Clinica, primary_key=True, on_delete=models.CASCADE)
    nome_cli = models.CharField(max_length=40)

class TelefoneClinica(models.Model):
    cod_cli = models.OneToOneField(Clinica, primary_key=True, on_delete=models.CASCADE)
    telefone_cli = models.CharField(max_length=16)

class EmailClinica(models.Model):
    cod_cli = models.OneToOneField(Clinica, primary_key=True, on_delete=models.CASCADE)
    email_cli = models.CharField(max_length=40)

class Especialidade(models.Model):
    cod_espec = models.CharField(primary_key=True, max_length=7)
    nome_espec = models.CharField(max_length=25)
    descricao = models.TextField()

class Medico(models.Model):
    cod_med = models.CharField(primary_key=True, max_length=7)
    genero = models.CharField(max_length=40)
    cod_espec = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

class NomeMedico(models.Model):
    cod_med = models.OneToOneField(Medico, primary_key=True, on_delete=models.CASCADE)
    nome_med = models.CharField(max_length=40)

class TelefoneMedico(models.Model):
    cod_med = models.OneToOneField(Medico, primary_key=True, on_delete=models.CASCADE)
    telefone_med = models.CharField(max_length=16)

class EmailMedico(models.Model):
    cod_med = models.OneToOneField(Medico, primary_key=True, on_delete=models.CASCADE)
    email_med = models.CharField(max_length=50, unique=True)

class ClinicaMedico(models.Model):
    cod_cli = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    cod_med = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_ingresso = models.DateField()
    carga_horaria_semanal = models.DecimalField(max_digits=3, decimal_places=1, default=20.0)
    class Meta:
        unique_together = ('cod_cli', 'cod_med')
