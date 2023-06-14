from django.shortcuts import render
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from .models import Pagamento
from ordine.models import Ordine
from django.shortcuts import redirect
# Create your views here.


class PagamentoListView(ListView):
    model = Pagamento
    template_name = "pagamento.html"

def paga_ordine (request, ordine_id):
    if request.user.is_authenticated:
        ordine = Ordine.objects.get(pk = ordine_id)
        pagamento = Pagamento.objects.create(id_ordine = ordine, id_cliente = request.user)
        pagamento.save()
        ordine.stato_ordine = "pagato"
        ordine.save()    
        return redirect('lista_ordini') 
    return redirect('login')