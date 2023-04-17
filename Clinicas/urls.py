"""
URL configuration for Clinicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clinicasmedicas.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("clinicaform/", criar_clinica, name="clinicaform"),
    path("medicoform/", criar_medico, name="medicoform"),
    path("especialidadeform/", criar_especialidade, name="especialidadeform"),
    path("clinica_medico_form/", add_clinica_medico, name="clinica_medico_form"),
    path("edit_clinica/<int:cod_cli>/", edit_clinica, name='edit_clinica'),
    path("update_clinica/<int:cod_cli>/", update_clinica, name='update_clinica'),
    path("edit_especialidade/<int:cod_espec>/", edit_especialidade, name='edit_especialidade'),
    path("update_especialidade/<int:cod_espec>/", update_especialidade, name='update_especialidade'),
    path("edit_medico/<int:cod_med>/", edit_medico, name='edit_medico'),
    path("update_medico/<int:cod_med>/", update_medico, name='update_medico'),
    path("edit_clinica_medico/<int:cod_cli>/", edit_clinica_medico, name='edit_clinica_medico'),
    path("update_clinica_medico/<int:cod_cli>/", update_clinica_medico, name='update_clinica_medico'),
    path("delete_clinica/<int:cod_cli>/", delete_clinica, name="delete_clinica"),
    path("delete_medico/<int:cod_med>/", delete_medico, name="delete_medico"),
    path("delete_espec/<int:cod_espec>/", delete_especialidade, name="delete_espec"),
    path("delete_meta/<int:id>/", delete_meta, name="delete_meta"),
]
