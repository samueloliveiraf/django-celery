from django.views.generic import (
    ListView
)
from .models import Produto


class ListViewProduct(ListView):
    template_name = 'home.html'
    model = Produto
