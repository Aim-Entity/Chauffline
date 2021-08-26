from django.shortcuts import render


def fleet(request):
    context = {

    }
    return render(request, "fleet/fleet.html", context)
