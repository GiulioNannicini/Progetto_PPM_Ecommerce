from django.db import models

from ordine.models import Ordine
from prodotto.models import Prodotto

# Create your models here.

class Elemento_Ordine(models.Model):
    id_ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE, related_name='elementi_ordine')
    id_prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita_del_prodotto = models.IntegerField()
    prezzo_del_prodotto = models.DecimalField(decimal_places=2, max_digits=11)

    def __str__(self) -> str:
        return str(self.id_ordine) + " " + str(self.id_prodotto) 
    
    class Meta:
        verbose_name_plural = 'Elemento_ordine'
