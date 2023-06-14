from django.db import models

from cliente.models import Cliente
from prodotto.models import Prodotto

# Create your models here.

class Carrello (models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='elementi_carrello')
    id_prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE, related_name='prodotti')
    quantita = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id_cliente) + " " + str(self.id_prodotto)
    
    class Meta:
        verbose_name_plural = 'Carrelli'