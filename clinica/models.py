from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome
    
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=6)
    telefone = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='medicos')

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    data_hora = models.DateField()
    observacoes = models.TextField()
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='consultas')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='consultas')

    def __str__(self):
        return f"{self.data_hora}, {self.observacoes} "
    
class Receita(models.Model):
    data_emissao = models.DateTimeField()
    consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE, related_name='receita')
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE, related_name='receita')
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='receita')

    def __str__(self):
        return self.data_emissao