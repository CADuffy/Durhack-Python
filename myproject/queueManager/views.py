from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from .models import PhoneNumber


def index(request):
    return render(request, "index.html", {})

def waiting(request):
    inp_value = request.GET.get("id")
    # add inp_value to mysql database
    entry = PhoneNumber(numbers0=inp_value)
    entry.save()
    numbers = PhoneNumber.objects.raw("SELECT * FROM main.queues WHERE numbers0 = " + inp_value)
    last = 0;
    for num in numbers:
        last = num.pos
    return render(request, "waiting.html", {"number": last})

def front(request):
    return render(request, "front.html", {})

def company(request):
    if request.GET.get('next-person'):
        PhoneNumber.objects.raw("DELETE FROM main.queues LIMIT 1")

    first = PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")
    last = PhoneNumber.objects.raw("SELECT * FROM main.queues ORDER BY  pos DESC LIMIT 1")

    actualLast = last[0].pos - (first[0].pos -1)

    return render(request, "company waiting.html", {"last": actualLast})