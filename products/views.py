from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World')

def create(request):
    return HttpResponse('New Product')
