from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class Cliente(AbstractUser, AbstractBaseUser):
    indirizzo = models.CharField(max_length=255)
    citta = models.CharField(max_length=255)
    stato = models.CharField(max_length=255)
    telefono = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

    class Meta:
        verbose_name_plural = "Clienti"
