from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def dataset(request):
    return render(request, 'dataset.html', {})


def conclude(request):
    return render(request, 'conclude.html', {})


def analysis(request):
    return render(request, 'analysis.html', {})


