from typing import Any, Dict
from django import http
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from django.shortcuts import redirect
from .models import Prodotto, Categoria
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.db.models import Q

# A page representing a list of objects.
#While this view is executing, self.object_list will contain the list of objects (usually, but not necessarily a queryset) that the view is operating upon.
   
class ProdottoListView(ListView):
    model = Prodotto
    template_name = "prodotto_list.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        if query is None:
            query = ''
        object_list = Prodotto.objects.filter(
            Q(nome_prodotto__icontains=query) | Q(descrizione__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            elementi_carrello_utente = self.request.user.elementi_carrello.all()
            context["totale_prezzo_carrello"] = sum([elemento.quantita * elemento.id_prodotto.prezzo for elemento in elementi_carrello_utente])
            context["totale_elementi_carrello"] = sum([elemento.quantita for elemento in elementi_carrello_utente])

        return context
     

# While this view is executing, self.object will contain the object that the view is operating upon.
class ProdottoDetailView(DetailView):  # new
    model = Prodotto
    template_name = "prodotto_detail.html"

# A view that displays a form for editing an existing object, redisplaying the form with validation errors (if there are any) and saving changes to the object.
# This uses a form automatically generated from the object’s model class (unless a form class is manually specified).

class ProdottoUpdateView(UpdateView):  # new
    
    model = Prodotto
    fields = (
        "nome_prodotto",
        "categoria",
        "descrizione",
        "prezzo",
        "immagine",
    )
    template_name = "prodotto_edit.html"
    

# A view that displays a confirmation page and deletes an existing object. The given object will only be deleted if the request method is POST.
# If this view is fetched via GET, it will display a confirmation page that should contain a form that POSTs to the same URL.
class ProdottoDeleteView(DeleteView):  # new
    model = Prodotto
    template_name = "prodotto_delete.html"

    # reverse_lazy won't execute until the value is needed.
    success_url = reverse_lazy("prodotto_list")

# A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
#@permissio_Required
class ProdottoCreateView(CreateView):  # new
    model = Prodotto
    template_name = "prodotto_new.html"
    fields = [
        "categoria",
        "nome_prodotto",
        "descrizione",
        "immagine",
        "prezzo",
        
    ]
    success_url = reverse_lazy("prodotto_list")
   
class CategoriaCreateView(CreateView):  # new
    model = Categoria
    template_name = "categoria_new.html"
    fields = [
        "nome_categoria",
        "immagine_categoria",   
    ]
    success_url = reverse_lazy("prodotto_list")
  
  

class CategoriaDetailView(DetailView):  # new
    model = Categoria
    template_name = "prodotto_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.get_object().prodotti.all()
        return context



def categorie (request):
    return{
        'categorie': Categoria.objects.all()
    }


def categoria_home(request):
    return {
        'cate': Categoria.objects.all()
    }
