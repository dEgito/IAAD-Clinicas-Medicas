from django.shortcuts import render, redirect
from clinicasmedicas.forms import ClinicaForm
# Create your views here.
def home(request):
    return render(request, "index.html")

def form(request):
    data = {}
    data['form'] = ClinicaForm()
    return render(request, "form.html", data)

def create(request):
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    
def edit(request):
    data = {}
    data['edit'] = ClinicaForm()
    return render(request, "edit.html", data)