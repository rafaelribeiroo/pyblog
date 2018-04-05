# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Iniciando o blog")
