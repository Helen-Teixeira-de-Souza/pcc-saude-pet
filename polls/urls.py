from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('meus-pets/', views.lista_pets, name='pagina_inicial'),
    path('vacinas/', views.historico_vacinas, name='pagina_vacinas'),
    path('consultas/', views.registro_consultas, name='pagina_consultas'),
]