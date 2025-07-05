from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Paciente, Especialidade, Consulta, Medicamento, Medico, Receita_medicamento, Receita
from .serializers import EstadoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = EstadoSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EstadoSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = EstadoSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = EstadoSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = EstadoSerializer

class Receita_medicamentoViewSet(ModelViewSet):
    queryset = Receita_medicamento.objects.all()
    serializer_class = EstadoSerializer

class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = EstadoSerializer