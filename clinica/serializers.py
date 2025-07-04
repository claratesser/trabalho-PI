from rest_framework.serializers import ModelSerializer
from .models import Medicamento, Especialidade, Medico, Consulta, Receita, Paciente, Receita_medicamento

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Receita_medicamento
        fields = '__all__'