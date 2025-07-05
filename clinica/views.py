from rest_framework.viewsets import ModelViewSet
from .models import Paciente, Especialidade, Consulta, Medicamento, Medico, Receita_medicamento, Receita
from .serializers import EstadoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class Receita_medicamentoViewSet(ModelViewSet):
    queryset = Receita_medicamento.objects.all()
    serializer_class = Receita_medicamentoSerializer

class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
