from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Car
from .filters import CarFilter

# def fleet(request):
#     context = {

#     }
#     return render(request, "fleet/fleet.html", context)


class FleetAllListView(ListView):
    template_name = "fleet/fleet.html"
    queryset = Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class FleetFirstClassListView(ListView):
    template_name = "fleet/fleet_first_class.html"
    queryset = Car.objects.filter(category="First Class")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class FleetExecutiveListView(ListView):
    template_name = "fleet/fleet_executive.html"
    queryset = Car.objects.filter(category="Executive")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class FleetBusinessListView(ListView):
    template_name = "fleet/fleet_business.html"
    queryset = Car.objects.filter(category="Business")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class FleetLargeListView(ListView):
    template_name = "fleet/XL.html"
    queryset = Car.objects.filter(category="XL")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class FleetAllDetailView(DetailView):
    template_name = "fleet/fleet_detail.html"
    queryset = Car.objects.all()
