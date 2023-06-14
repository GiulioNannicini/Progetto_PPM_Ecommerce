from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ClienteCreationForm


class SignUpView(CreateView):
    form_class = ClienteCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
