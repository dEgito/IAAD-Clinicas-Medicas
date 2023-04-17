from django.shortcuts import render, redirect
from clinicasmedicas.forms import *
from clinicasmedicas.models import Clinica, Especialidade, Medico, ClinicaMedico

# Create your views here.
def home(request):
    data = {}
    data['clinica'] = Clinica.objects.all()
    data['especialidade'] = Especialidade.objects.all()
    data['medico'] = Medico.objects.all()
    data['clinicamedico'] = ClinicaMedico.objects.all()
    return render(request, 'index.html', data)

def criar_clinica(request):
    form= ClinicaForm()
    if request.method == 'POST':
        form= ClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'clinicaform.html', {'form': form})

def criar_medico(request):
    if request.method == 'POST':
        form_medico = MedicoForm(request.POST)
        if form_medico.is_valid():
            form_medico.save()
            return redirect('home')
    else:
        form_medico = MedicoForm()

    return render(request, 'medicoform.html', {'form': form_medico})


def criar_especialidade(request):
    if request.method == 'POST':
        form_espec= EspecialidadeForm(request.POST)
        if form_espec.is_valid():
            form_espec.save()
            return redirect('home')
    else:
        form_espec= EspecialidadeForm()
    return render(request, 'especialidadeform.html', {'form': form_espec})

def add_clinica_medico(request):
    if request.method == 'POST':
        form_climed = ClinicaMedicoForm(request.POST)
        if form_climed.is_valid():
            form_climed.save()
            return redirect('home')
    else:
        form_climed = ClinicaMedicoForm()
    return render(request, 'clinica_medico_form.html', {'form': form_climed})

def edit(request):
    form= ClinicaForm()
    if request.method == 'POST':
        form= ClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'edit.html', {'form': form})

def delete_clinica(request, cod_cli):
    db = Clinica.objects.get(pk=cod_cli)
    db.delete()
    return redirect("home")

def delete_medico(request, cod_med):
    db = Medico.objects.get(pk=cod_med)
    db.delete()
    return redirect("home")

def delete_especialidade(request, cod_espec):
    db = Especialidade.objects.get(pk=cod_espec)
    db.delete()
    return redirect("home")

def delete_meta(request, id):
    db = ClinicaMedico.objects.get(pk=id)
    db.delete()
    return redirect("home")