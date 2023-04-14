from django.forms import ModelForm, modelformset_factory
from clinicasmedicas.models import *

#Create the form class.

class EnderecoClinicaForm(ModelForm):
    class Meta:
        model = EnderecoClinica
        fields = ('cod_end_clinica', 'rua_cli', 'bairro_cli', 'cep_cli', 'numero_end_cli')

class ClinicaForm(ModelForm):
    class Meta:
        model = Clinica
        fields = ('cod_cli', 'cod_end_clinica')

class NomeClinicaForm(ModelForm):
    class Meta:
        model = NomeClinica
        fields = ('cod_cli', 'nome_cli')

class TelefoneClinicaForm(ModelForm):
    class Meta:
        model = TelefoneClinica
        fields = ('cod_cli', 'telefone_cli')

class EmailClinicaForm(ModelForm):
    class Meta:
        model = EmailClinica
        fields = ('cod_cli', 'email_cli')

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ('cod_espec', 'nome_espec', 'descricao')

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ('cod_med', 'genero', 'cod_espec')

class NomeMedicoForm(ModelForm):
    class Meta:
        model = NomeMedico
        fields = ('cod_med', 'nome_med')

class TelefoneMedicoForm(ModelForm):
    class Meta:
        model = TelefoneMedico
        fields = ('cod_med', 'telefone_med')

class EmailMedicoForm(ModelForm):
    class Meta:
        model = EmailMedico
        fields = ('cod_med', 'email_med')

class ClinicaMedicoForm(ModelForm):
    class Meta:
        model = ClinicaMedico
        fields = ('cod_cli', 'cod_med', 'data_ingresso', 'carga_horaria_semanal')