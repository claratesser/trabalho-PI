from django.contrib import admin

from django.contrib import admin
from .models import Medicamento, Especialidade

admin.site.register(Medicamento)
admin.site.register(Especialidade)