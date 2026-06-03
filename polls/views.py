from django.shortcuts import get_object_or_404, render, redirect
from .models import Consulta, Pet, Vacina
from .forms import PetForm, VacinaForm

# Pet
def lista_pets(request):
    todos_os_pets = Pet.objects.all()
    context = {'lista_pets': todos_os_pets}
    return render(request, 'polls/lista_pets.html', context)

def detalhes_pet(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    context = {'pet': pet}
    return render(request, 'polls/detalhes_pet.html', context)

def novo_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('polls:lista_pets')
    return render(request, 'polls/pet_form.html', {'form': form})

def editar_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('polls:lista_pets')
    return render(request, 'polls/pet_form.html', {'form': form})

def deletar_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('polls:lista_pets')

# Vacina
def historico_vacinas(request):
    todas_as_vacinas = Vacina.objects.all().select_related('pet')
    context = {'lista_vacinas': todas_as_vacinas}
    return render(request, 'polls/vacinas.html', context)

def nova_vacina(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    form = VacinaForm(request.POST or None)
    if form.is_valid():
        vacina = form.save(commit=False)
        vacina.pet = pet
        vacina.save()
        return redirect('polls:detalhes_pet', pet_id=pet.id)
    return render(request, 'polls/vacina_form.html', {'form': form, 'pet': pet})

def editar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    form = VacinaForm(request.POST or None, instance=vacina)
    if form.is_valid():
        form.save()
        return redirect('polls:detalhes_pet', pet_id=vacina.pet.id)
    return render(request, 'polls/vacina_form.html', {'form': form, 'pet': vacina.pet})

def deletar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    pet_id = vacina.pet.id
    vacina.delete()
    return redirect('polls:detalhes_pet', pet_id=pet_id)

# Consulta
def registro_consultas(request):
    todas_as_consultas = Consulta.objects.all().select_related('pet')
    context = {'lista_consultas': todas_as_consultas}
    return render(request, 'polls/consultas.html', context)