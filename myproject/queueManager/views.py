from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.db import connection

from .models import PhoneNumber
from .models import companyRecord


def initialise(request):
    return render(request, "first opening.html", {})


def index(request):
    return render(request, "index.html", {})


def waiting(request):
    inp_value = request.GET.get("id")
    # add inp_value to mysql database
    entry = PhoneNumber(numbers0=inp_value)
    entry.save()
    return render(request, "waiting.html", {"number": get_last()})


def front(request):
    return render(request, "front.html", {})


def company(request):
    return render(request, "company waiting.html", {"last": get_last()})


def company_register(request):
    return render(request, "company.html", {})


def register_company(request):
    entry = companyRecord(company_name=request.GET.get("company-name"),
                          company_password=request.GET.get("company-pass"),
                          company_type=request.GET.get("company-type"))
    entry.save()
    connection.cursor().execute("ALTER TABLE main.queues ADD " + request.GET.get("company-name") + " Text")
    return render(request, "company waiting.html", {"number": 0})


def nextperson(request):
    PhoneNumber.objects.filter(pos = PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")[0].pos).delete()
    return redirect(company)


def get_last():
    first = PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")
    last = PhoneNumber.objects.raw("SELECT * FROM main.queues ORDER BY pos DESC LIMIT 1")
    return last[0].pos - (first[0].pos - 1)


def get_first():
    return PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")