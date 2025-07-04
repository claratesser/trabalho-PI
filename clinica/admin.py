from django.contrib import admin

from django.contrib import admin
from .models import Medicamento, Especialidade, Paciente

admin.site.register(Medicamento)
admin.site.register(Especialidade)
admin.site.register(Paciente)