from django.urls import path
from . import views

urlpatterns = [
    path("", views.FleetAllListView.as_view(), name="fleet"),
    path("first-class/", views.FleetFirstClassListView.as_view(), name="first-class"),
    path("executive/", views.FleetExecutiveListView.as_view(), name="executive"),
    path("business/", views.FleetBusinessListView.as_view(), name="business"),
    path("xl/", views.FleetLargeListView.as_view(), name="xl"),
    path("item/<str:slug>", views.FleetAllDetailView.as_view(), name="fleet-detail")
]
