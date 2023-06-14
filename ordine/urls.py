from django.urls import path

from .views import OrdineListView, OrdineDetailView
from . import views

urlpatterns = [
    path('', OrdineListView.as_view(), name="lista_ordini" ),
    path('new/', views.crea_ordine_da_carrello, name='crea_ordine'),
    path('<int:pk>/', OrdineDetailView.as_view(), name='dettaglio_ordine'),
   
]
