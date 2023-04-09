from django.forms import ModelForm
from clinicasmedicas.models import Clinica, ClinicaMedico, Medico, Especialidade

# Create the form class.
class ClinicaForm(ModelForm):
     class Meta:
         model = Clinica
         fields = ["CodCli", "NomeCli", "Endereco", "Telefone", "Email"]
