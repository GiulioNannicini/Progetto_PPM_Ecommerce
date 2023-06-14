from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from carrello.models import Carrello
from .models import Ordine
from elemento_ordine.models import Elemento_Ordine
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new 
from typing import Any, Dict

# Create your views here.


class OrdineListView(ListView):
    model = Ordine
    template_name = "ordine.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.request.user.ordini.all()
        return context


def crea_ordine_da_carrello(request):
    if request.user.is_authenticated:
        elementi_carrello = Carrello.objects.filter(id_cliente = request.user)
        ordine = Ordine.objects.create(id_cliente = request.user)
        ordine.save()
        for elemento_carrello in elementi_carrello:
            elemento_ordine = Elemento_Ordine.objects.create(id_ordine = ordine, id_prodotto = elemento_carrello.id_prodotto, quantita_del_prodotto = elemento_carrello.quantita, prezzo_del_prodotto = elemento_carrello.id_prodotto.prezzo )
            elemento_ordine.save()
        Carrello.objects.filter(id_cliente = request.user).delete()
        return redirect('lista_ordini') 
   

class OrdineDetailView(DetailView):
    model = Ordine
    template_name = "dettaglio_ordine.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        elementi_ordine = self.get_object().elementi_ordine.all()
        context["object_list"] =  self.get_object().elementi_ordine.all()
        context["totale_prezzo_ordine"] = sum([elemento.quantita_del_prodotto * elemento.id_prodotto.prezzo for elemento in elementi_ordine])
        context["totale_elementi_ordine"] = sum([elemento.quantita_del_prodotto for elemento in elementi_ordine])

        return context
        
