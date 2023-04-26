from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

# Create your views here.

class Cow:
    def __init__ (self, name):
        self.name = name


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

def hello2(request):
    return render(
        request,
        'next_app/hello.html'
    )

def name2(request, data):
    return render(
        request,
        'name.html',
        context={
            "data": data
        }
    )
#widok - warstwa logiki
# szablon = warstwa prexzentacji (DTL- Django Template Language
def is_it_new_year(request):
    now = datetime.now()
    is_it_new_year = False
    if now.day == 1 and now.month == 1:
        is_it_new_year = True
    return render(
        request,
        'is_it_new_year.html',
        context={
        }
    )

def fruits(request):
    fruits_list = [
        'jabłko',
        'banan',
        'winogrona',
        'mandarynki',
    ]

    person = {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 15,
    }

    cow = Cow(name="Mućka")
    return render(
        request,
        'fruits.html',
        context={
            'fruits': fruits_list,
            'person': person,
            'cow': cow,

        })





