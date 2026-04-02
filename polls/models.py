from django.db import models

class Pet(models.Model):
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