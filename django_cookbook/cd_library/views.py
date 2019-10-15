from django.shortcuts import render
from django.http import HttpResponse
from .models import CD

# Create your views here.

def index(request):
    query_set = CD.objects.all()
    context = {
        'cds': query_set
    }
    return render(request, 'cd_library/index.html', context)

def detail(request, pk):
    query_set = CD.objects.get(pk=pk)
    context = {
        'cd': query_set
    }
    return render(request, 'cd_library/detail.html', context)