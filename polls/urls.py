from django.urls import path, include
from . import views

app_name = 'polls' 

urlpatterns = [
    path('lista-pets/', views.lista_pets, name='lista_pets'),
    path('detalhes-pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),
    path('novo/', views.novo_pet, name='novo_pet'),
    path('edit/<int:pk>/', views.editar_pet, name='editar_pet'),
    path('del/<int:pk>/', views.deletar_pet, name='deletar_pet'),
    path('pet/<int:pet_id>/vacina/nova/', views.nova_vacina, name='nova_vacina'),
    path('vacinas/', views.historico_vacinas, name='pagina_vacinas'),
    path('vacina/<int:pk>/editar/', views.editar_vacina, name='editar_vacina'),
    path('vacina/<int:pk>/deletar/', views.deletar_vacina, name='deletar_vacina'),
    path('consultas/', views.registro_consultas, name='pagina_consultas'),
    path('accounts/', include('django.contrib.auth.urls')), 
]