from django.shortcuts import render
from apps.produtos.views import Produto


def home(request):
    produtos = Produto.objects.filter(ativo=True)

    context = {
        'produtos': produtos
    }

    return render(request, 'home.html', context)
