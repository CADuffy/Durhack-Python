from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {})

def waiting(request):
    return render(request, "waiting.html", {"number": 12})

def front(request):
    return render(request, "front.html", {})