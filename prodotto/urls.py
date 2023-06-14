from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ProdottoListView,
    ProdottoDetailView,
    ProdottoUpdateView,
    ProdottoDeleteView,
    ProdottoCreateView,  # new
    CategoriaCreateView,
    CategoriaDetailView,
)

from . import views

urlpatterns = [
    path("<int:pk>/", ProdottoDetailView.as_view(), name="prodotto_detail"),
    path("<int:pk>/edit/", ProdottoUpdateView.as_view(), name="prodotto_edit"),
    path("<int:pk>/delete/", ProdottoDeleteView.as_view(), name="prodotto_delete"),
    path("new/", ProdottoCreateView.as_view(), name="prodotto_new"),
    path("", ProdottoListView.as_view(), name="prodotto_list"),
    path("categorie/<int:pk>/", CategoriaDetailView.as_view() , name="categoria_detail"),
    path("categorie/new", CategoriaCreateView.as_view(), name="categoria_new"),
    path("homecategoria/", views.categoria_home, name='categoria_home'),
    
]