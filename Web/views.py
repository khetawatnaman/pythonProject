from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def login(request):
    return render(request, 'index.html', context=None)


def naman(request):
    return render(request, 'Naman.html', context=None)


def hitesh(request):
    return render(request, 'Hitesh.html', context=None)


def nishit(request):
    return render(request, 'Nishit.html', context=None)
