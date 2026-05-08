from django.shortcuts import render
from .models import Consulta, Pet, Vacina

def lista_pets(request):
    todos_os_pets = Pet.objects.all()
    context = {'lista_pets': todos_os_pets}
    return render(request, 'polls/lista_pets.html', context)

def detalhes_pet(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    context = {'pet': pet}
    return render(request, 'polls/detalhes_pet.html', context)

def historico_vacinas(request):
    todas_as_vacinas = Vacina.objects.all().select_related('pet')
    context = {'lista_vacinas': todas_as_vacinas}
    return render(request, 'polls/vacinas.html', context)

def registro_consultas(request):
    todas_as_consultas = Consulta.objects.all().select_related('pet')
    context = {'lista_consultas': todas_as_consultas}
    return render(request, 'polls/consultas.html', context)