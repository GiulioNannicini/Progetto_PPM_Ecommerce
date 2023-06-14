from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class HomePage(TemplateView):
    template_name = "home.html"

class Privacy (TemplateView):
    template_name = "privacy.html"