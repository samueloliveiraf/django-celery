from django.db import models


class Produto(models.Model):
    nome = models.CharField(
        blank=True,
        null=True, verbose_name='Nome ',
        max_length=350
    )
    quantidade = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Quantidade '
    )
    ativo = models.BooleanField(
        verbose_name='Ativo: ',
        default=True
    )

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome
