from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world")

def Ilona(request):
    return HttpResponse("<h2 > Witaj <span style='color: red'>, Ilona</span></h2>")

def hi(request):
    return HttpResponse("")

def hi2(request):
    return render(request, 'hi.html')

def pikatchu(request):
    return render(request, 'pikatchu.html')

def pokemonGo(request):
    return render(request, 'pokemonGo.html')