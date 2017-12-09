from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #text = "Enter ID:"
    return render(request, "index.html", {})

def waiting(request):
    text = "Waiting..."
    return render(request, "waiting.html", {})

def front(request):
    text = "Front of queue"
    return HttpResponse(text)