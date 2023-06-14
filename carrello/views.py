from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from .models import Carrello
from prodotto.models import Prodotto
import json
from django.contrib import messages
from typing import Any, Dict
# Create your views here.

class CarrelloListView(ListView):
    model = Carrello
    template_name = "carrello.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        elementi_carrello_utente = self.request.user.elementi_carrello.all()
        context["object_list"] = elementi_carrello_utente
        context["totale_prezzo_carrello"] = sum([elemento.quantita * elemento.id_prodotto.prezzo for elemento in elementi_carrello_utente])
        context["totale_elementi_carrello"] = sum([elemento.quantita for elemento in elementi_carrello_utente])
        return context
    

def aggiungi_prodotti_al_carrello(request, prodottoId):
    prodotto = get_object_or_404(Prodotto, pk=prodottoId)
    if request.user.is_authenticated:
        elemento_carrello, created = Carrello.objects.get_or_create(id_cliente = request.user , id_prodotto = prodotto)
        elemento_carrello.quantita += 1
        elemento_carrello.save()
        messages.success(request, 'Carrello aggiornato!')
        return redirect('prodotto_list') 
    return redirect('login')     

def elimina_elementi_dal_carrello(request, carrelloId):
    if request.user.is_authenticated:
        Carrello.objects.filter(id = carrelloId).delete()
    return redirect('carrello')   


def aumenta_quantita_carrello(request, carrelloId):
    elemento_carrello = get_object_or_404(Carrello, pk=carrelloId)
    if request.user.is_authenticated:
        elemento_carrello.quantita += 1
        elemento_carrello.save()
    return redirect('carrello')      


def diminuisci_quantita_carrello(request, carrelloId):
    elemento_carrello = get_object_or_404(Carrello, pk=carrelloId)
    if request.user.is_authenticated:
        elemento_carrello.quantita -= 1
        elemento_carrello.save()
    return redirect('carrello')      