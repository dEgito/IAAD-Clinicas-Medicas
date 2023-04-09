from django.shortcuts import render
from clinicasmedicas.forms import ClinicaForm
# Create your views here.
def home(request):
    return render(request, "index.html")

def form(request):
    data = {}
    data['form'] = ClinicaForm()
    return render(request, "form.html", data)