from django.db import models

from ordine.models import Ordine
from cliente.models import Cliente
import datetime
# Create your models here.

class Pagamento(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField(default= datetime.datetime.now())

    class Meta:
        verbose_name_plural = ("Pagamenti")

    def __str__(self):
        return str(self.id_cliente) + " " + str(self.id_ordine)

    