
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clinica.views import MedicoViewSet, MedicamentoViewSet, EspecialidadeViewSet, ConsultaViewSet, ReceitaViewSet, PacienteViewSet, Receita_medicamentoViewSet

router = DefaultRouter()

router.register(r'medicos', MedicoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'especialidades', EspecialidadeViewSet,)
router.register(r'consultas', ConsultaViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'receita_medicamentos', Receita_medicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]