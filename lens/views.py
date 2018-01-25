from django.shortcuts import render

from django.views.generic import ListView
from .models import Lens
# Create your views here.

class IndexView(ListView):
    template_name='index.html'
    headline = 'home'
    model = Lens

    def get_queryset(self):
        return super().get_queryset()