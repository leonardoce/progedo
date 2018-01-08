from django.shortcuts import render
from django.http import HttpResponse


def ciao(request):
    return HttpResponse("ciao")


def index(request):
    return render(request, "blog/index.html", {})