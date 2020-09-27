from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView)
from pet.models import Pet

# Create your views here.

class ViewIndex(TemplateView):
    template_name = 'index.html'

class ViewAbout(TemplateView):
    template_name = 'about.html'

class ListViewPet(ListView):
    template_name = 'pets_list.html'
    model = Pet

class ViewPet(DetailView):
    template_name = 'pet_detail.html'
    model = Pet

