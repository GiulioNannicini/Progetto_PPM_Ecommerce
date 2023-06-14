from django.db import models

from django.urls import reverse

# Create your models here.
class Categoria(models.Model): 
    nome_categoria = models.CharField(max_length=255, unique=True)   
    immagine_categoria = models.ImageField(upload_to='immagini_categoria/', default="logobg.png")    

    def __str__(self):
        return self.nome_categoria
    
    def get_absolute_url(self):
       return reverse("categoria_detail", kwargs={"pk": self.pk})


    class Meta:
        verbose_name_plural = "Categorie"


class Prodotto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='prodotti')
    nome_prodotto = models.CharField(max_length=255)
    descrizione = models.TextField()
    prezzo = models.DecimalField(decimal_places=2, max_digits=11)
    immagine = models.ImageField(upload_to='immagini_prodotti/', default="logobg.png")

    def __str__(self):
        return self.nome_prodotto
    
    def get_absolute_url(self):
        return reverse("prodotto_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Prodotti"
