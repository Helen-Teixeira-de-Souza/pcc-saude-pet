from django.db import models

class Pet(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='pets')
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50, blank=True)
    peso_atual = models.FloatField(help_text="Peso em kg")
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Vacina(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    nome_vacina = models.CharField(max_length=200)
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_vacina} - {self.pet.nome}"
    
class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    motivo = models.CharField(max_length=255)
    diagnostico = models.TextField(blank=True)
    prescricao = models.TextField(blank=True)
    
    def __str__(self):
        return f"Consulta {self.pet.nome} - {self.data_consulta}"

class HistoricoPeso(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='historico_peso')
    peso = models.FloatField(help_text="Peso em kg")
    data_pesagem = models.DateField(auto_now_add=True) # para salvar a data automaticamente

    def __str__(self):
        return f"{self.pet.nome} - {self.peso}kg em {self.data_pesagem}"
    
class Tutor(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome