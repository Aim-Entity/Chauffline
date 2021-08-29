from django.shortcuts import render
from .models import Testimonials, PopularCar


def index(request):
    popular_cars = PopularCar.objects.all()[:3]
    testimonials = Testimonials.objects.all()[:3]
    context = {
        "testimonials": testimonials,
        "cars": popular_cars
    }
    return render(request, "home/index.html", context)
