from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path(' ', views.lista_pets, name='lista_pets'),
    path('meus-pets/', views.lista_pets, name='lista_pets'),
    path('detalhes-pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),
    path('vacinas/', views.historico_vacinas, name='pagina_vacinas'),
    path('consultas/', views.registro_consultas, name='pagina_consultas'),
    path('novo/', views.novo_pet, name='novo_pet'),
    path('edit/<int:pk>/', views.editar_pet, name='editar_pet'),
    path('del/<int:pk>/', views.deletar_pet, name='deletar_pet'),
]