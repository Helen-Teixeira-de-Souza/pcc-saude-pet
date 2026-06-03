from django import forms
from .models import Pet, Vacina

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'especie', 'raca', 'peso_atual', 'data_nascimento']

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['pet', 'nome_vacina', 'data_aplicacao', 'proxima_dose', 'veterinario', 'observacoes']