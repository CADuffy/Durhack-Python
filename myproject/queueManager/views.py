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
    connection.cursor().execute("INSERT INTO  main." + request.GET.get('queue-name') + " VALUES (" +
                                request.GET.get('phone-number') + ")")
    return render(request, "waiting.html", {"number": get_last(request.GET.get('queue-name'))})


def front(request):
    return render(request, "front.html", {})


def company_register(request):
    return render(request, "company.html", {})


def register_company(request):
    entry = companyRecord(company_name=request.GET.get("company-name"),
                          company_password=request.GET.get("company-pass"),
                          company_type=request.GET.get("company-type"))
    entry.save()

    #Makes a queues table for the company
    connection.cursor().execute("CREATE TABLE main." + request.GET.get("company-name") + " (pos Text NOT NULL " +
                                "AUTO_INCREMENT, numbers Text)")
    return render(request, "company waiting.html", {"number": 0})


def login_company(request):
    company_name = request.GET.get("company-name")
    company_pass = request.GET.get("company-pass")
    c = connection.cursor().execute("SELECT * FROM main.companies")
    curr_row = null
    for row in c:
        if row.company-name == company_name:
            if row.company-name == company_pass:
                curr_row = row
    if curr_row == null:
        print("Details incorrect")
    else:
        return render(request, "company waiting.html", {"last": get_last(curr_row.company_name)})


def nextperson(request):
    PhoneNumber.objects.filter(pos = PhoneNumber.objects.raw("SELECT * FROM main." + ? + "LIMIT 1")[0].pos).delete()
    return redirect(company)


def get_last(table):
    first = PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")
    last = PhoneNumber.objects.raw("SELECT * FROM main.queues ORDER BY pos DESC LIMIT 1")
    return last[0].pos - (first[0].pos - 1)


def get_first():
    return PhoneNumber.objects.raw("SELECT * FROM main.queues LIMIT 1")
