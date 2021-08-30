from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Car


# def fleet(request):
#     context = {

#     }
#     return render(request, "fleet/fleet.html", context)


class FleetAllListView(ListView):
    template_name = "fleet/fleet.html"
    queryset = Car.objects.all()


class FleetAllDetailView(DetailView):
    template_name = "fleet/fleet_detail.html"
    queryset = Car.objects.all()
