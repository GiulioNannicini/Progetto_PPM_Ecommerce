from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Cliente


class ClienteCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "indirizzo",
            "citta",
            "stato",
            "telefono",
        ) 


class ClienteChangeForm(UserChangeForm):
    class Meta:
        model = Cliente
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "indirizzo",
            "citta",
            "stato",
            "telefono",

        )  
