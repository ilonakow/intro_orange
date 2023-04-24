from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")

def eva(request):
    return HttpResponse("Hello, <span style='color:red'>Eva<span/>!")

def adam(request):
    return HttpResponse("Hello, Adam!")

def name(request, data):
    return HttpResponse(f"Hello, {data}!")