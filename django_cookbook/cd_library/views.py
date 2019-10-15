from django.shortcuts import render
from django.http import HttpResponse
from .models import CD
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

class IndexView(ListView):
    model = CD
    template_name = 'cd_library/index.html'
    context_object_name = 'cds'

class DetailView(DetailView):
    model = CD
    template_name = 'cd_library/detail.html'
    context_object_name = 'cd'

class CreateView(CreateView):
    model = CD
    fields = '__all__'
    template_name = 'cd_library/create.html'
    success_url = reverse_lazy('cd_library:index')
    
class DeleteView(DeleteView):
    model = CD
    template_name = 'cd_library/delete.html'
    context_object_name = 'cd'
    success_url = reverse_lazy('cd_library:index')