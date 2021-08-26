from django.urls import path
from . import views

urlpatterns = [
    path("", views.fleet, name="fleet")
]
