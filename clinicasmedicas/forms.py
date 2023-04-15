from django.forms import ModelForm, modelformset_factory
from clinicasmedicas.models import *

#Create the form class.

from django import forms
from .models import Clinica, Especialidade, Medico, ClinicaMedico


class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = '__all__'


class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = '__all__'


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'


class ClinicaMedicoForm(forms.ModelForm):
    class Meta:
        model = ClinicaMedico
        fields = '__all__'