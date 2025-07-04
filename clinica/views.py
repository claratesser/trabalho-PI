from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Paciente, Especialidade, Consulta, Medicamento, Medico, Receita_medicamento, Receita
from .serializers import EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Receita_medicamento.objects.all()
    serializer_class = EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = EstadoSerializer