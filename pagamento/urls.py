from django.urls import path

from .views import PagamentoListView
from . import views

urlpatterns = [
    path('', PagamentoListView.as_view(), name="pagamento"),
    path('pagaOrdine/<int:ordine_id>/', views.paga_ordine, name='paga_ordine'),
]
