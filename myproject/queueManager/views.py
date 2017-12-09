from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

def index(request):
    return render(request, "index.html", {})

def waiting(request):
    inp_value = request.GET.get("id")
    # add inp_value to mysql database

    return render(request, "waiting.html", {"number": inp_value})

def front(request):
    return render(request, "front.html", {})