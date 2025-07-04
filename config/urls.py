"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clinica.views import MedicoViewSet, MedicamentoViewSet, EspecialidadeViewSet, ConsultaViewSet, ReceitaViewSet, PacienteViewSet, Receita_medicamentoViewSet

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet,)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

outer = DefaultRouter()
router.register(r'receita_medicamentos', Receita_medicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]