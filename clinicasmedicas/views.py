from django.shortcuts import render, redirect
from clinicasmedicas.forms import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def novo_cod_clinica(request):
    if request.method == 'POST':
        form_cod = ClinicaForm(request.POST)
        form_nome = NomeClinicaForm(request.POST)
        if form_cod.is_valid() and form_nome.is_valid() :
            form_cod.save()
            form_nome.save()
            return redirect('home') # redireciona para a página inicial
    else:
        form_cod = ClinicaForm()
        form_nome = NomeClinicaForm()
    return render(request, 'clinicaform.html', {'form1': form_cod, 'form2': form_nome})

def create(request):
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")