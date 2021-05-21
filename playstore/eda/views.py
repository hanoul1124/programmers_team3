from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def dataset(request):
    return render(request, 'dataset.html', {})


def conclude(request):
    return render(request, 'conclude.html', {})


def analysis(request):
    items = Item.objects.all()
    context = {'items': items,}
    return render(request, 'analysis.html', context)


