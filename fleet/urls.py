from django.urls import path
from . import views

urlpatterns = [
    path("", views.FleetAllListView.as_view(), name="fleet"),
    path("item/<str:slug>", views.FleetAllDetailView.as_view(), name="fleet-detail")
]
