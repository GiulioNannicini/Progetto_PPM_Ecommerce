from django.db import models
from cliente.models import Cliente
import datetime
from django.urls import reverse

# Create your models here.
x = [        
        ("inserito","inserito"),
        ("pagato","pagato"),
    ]
class Ordine(models.Model):
    
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE, related_name='ordini')
    data_ordine = models.DateTimeField( default = datetime.datetime.now() )
    stato_ordine = models.TextField(choices=x, default="inserito")
  
   # TextField( default='inserito')

  
    def __str__(self):
        return str(self.id_cliente) + " " + str(self.data_ordine)
    
    def get_absolute_url(self):
       return reverse("dettaglio_ordine", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name_plural = 'Ordine'