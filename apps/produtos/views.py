from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView
)
from .models import Produto


class ListViewProduct(ListView):
    template_name = 'home.html'
    model = Produto


class UpdateViewProduct(UpdateView):
    template_name = 'edit.html'
    model = Produto

    fields = [
        'nome',
        'quantidade',
        'ativo'
    ]

    success_url = reverse_lazy('home')

