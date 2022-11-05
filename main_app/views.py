from django.shortcuts import render
from django.http import HttpResponse

class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

cars = [
    Car('Mercedes-Benz', 'E-Class', '2022', 'red'),
    Car('Infiniti', 'Q40', '2015', 'black'),
    Car('Genesis', 'G80', '2019', 'white'),
]

# Create your views here.
def home(request):
    return HttpResponse("YOOOO")

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars })