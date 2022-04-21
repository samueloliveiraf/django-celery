from celery.utils.log import get_task_logger
from django_celery.celery import app
from .models import Produto


logger = get_task_logger(__name__)


@app.task(name='task_verificar_produtos', queue='queue_verificar_produtos')
def task_verificar_produtos():
    produtos = Produto.objects.all()

    for produto in produtos:
        if produto.quantidade == 0:
            produto.ativo = False
            produto.save()
