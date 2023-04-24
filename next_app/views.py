from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")

def eva(request):
    return HttpResponse("Hello,Eva!")
    # return HttpResponse("Hello, <span style='color:red'>Eva<span/>!")

def adam(request):
    return HttpResponse("Hello, Adam!")

def name(request, data):
    # XSS Cross Site Scripting
    # Podatnosc xss
    # Always remember to escape your output
    print(data)
    escaped_data = escape(data)
    print(escaped_data)

    return HttpResponse(f"Hello, {data}!")



