from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def lista_pets(request):
    return HttpResponse("<h1>Meus Pets</h1><p>Aqui aparece a lista de todos os seus animais registrados.</p>")

def historico_vacinas(request):
    return HttpResponse("<h1>Histórico de Vacinas</h1><p>Aqui registra as vacinas.</p>")

def registro_consultas(request):
    return HttpResponse("<h1>Registro de Consultas</h1><p>Aqui registra consultas.</p>")