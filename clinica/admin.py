from django.contrib import admin

from django.contrib import admin
from .models import Medicamento, Especialidade, Paciente, Medico, Consulta, Receita

admin.site.register(Medicamento)
admin.site.register(Especialidade)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Receita)