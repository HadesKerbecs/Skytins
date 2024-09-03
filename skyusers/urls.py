from django.urls import path
from .views import index, lista_clientes, adicionar_cliente, importar_dados

urlpatterns = [
    path('', index, name='index'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('adicionar/', adicionar_cliente, name='adicionar_cliente'),
    path('importar/', importar_dados, name='importar_dados'),
]
