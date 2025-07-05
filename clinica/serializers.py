from rest_framework.serializers import ModelSerializer
from .models import Medicamento, Especialidade, Medico, Consulta, Receita, Paciente, Receita_medicamento

class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ReceitaSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class Receita_medicamentoSerializer(ModelSerializer):
    class Meta:
        model = Receita_medicamento
        fields = '__all__'