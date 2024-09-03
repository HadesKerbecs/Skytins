from django.shortcuts import render
import pandas as pd
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages


def index(request):
    return render(request, 'skyusers/index.html')

def importar_planilha():
    arquivo = 'Usuarios.xlsx'

    try:
        df = pd.read_excel(arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    for index, row in df.iterrows():
        try:
            Cliente.objects.create(
                codigo=row['NOME'],
                nome=row['EMPRESA'],
                ip=row['IP'],
                cnpj=row['CNPJ'],
                qt_usuarios=row['USUÁRIOS'],
                grupo=row['MULTILOJA']
            )
        except Exception as e:
            print(f"Erro ao criar cliente: {e}")


def importar_dados(request):
    importar_planilha()
    messages.success(request, 'Dados importados com sucesso!')
    return redirect('lista_clientes')


def lista_clientes(request):
    query = request.GET.get('search', '')  # Obtém o parâmetro de pesquisa da URL
    if query:
        clientes = Cliente.objects.filter(nome__icontains=query)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'skyusers/index.html', {'clientes': clientes})


def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente adicionado com sucesso!')
            return redirect('lista_clientes')
        else:
            messages.error(request, 'Erro ao adicionar cliente.')
    else:
        form = ClienteForm()
    return render(request, 'skyusers/adicionar_cliente.html', {'form': form})


