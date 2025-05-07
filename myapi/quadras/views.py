from django.shortcuts import render, redirect
from .models import Quadra  # Importe o modelo Quadra
from django.db.models import Q
from .forms import QuadraForm
from django.contrib import messages


def home(request):
    # Obter o valor da pesquisa (campo "q")
    query = request.GET.get('q', '')  # Captura o valor do campo "q" no formulário (ou vazio se não houver valor)

    # Filtro inicial: Retorna todas as quadras se não houver busca
    if query:
        # Filtrar quadras por nome ou endereço (pesquisa case-insensitive)
        quadras = Quadra.objects.filter(
            Q(nome__icontains=query) | Q(endereco__icontains=query)
        )
    else:
        quadras = Quadra.objects.all()  # Retorna todas as quadras

    # Passar as quadras para o template
    return render(request, 'quadras/home.html', {'quadras': quadras, 'query': query})



def adicionar_quadra(request):
    if request.method == 'POST':
        form = QuadraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página sucesso.html
        else:
            messages.error(request, "Erro ao cadastrar a quadra. Verifique os dados.")  # Mantém no formulário com erro
    
    form = QuadraForm()
    return render(request, 'quadras/adicionar_quadra.html', {'form': form})


def sucesso(request):
    return render(request, 'quadras/sucesso.html')  


