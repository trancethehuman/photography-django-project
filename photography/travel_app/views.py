from django.shortcuts import render
from .models import PhotoTravel
# Create your views here.

def photo_list_travel(request):
    queryset = PhotoTravel.objects.all()
    context = {
        "photos":queryset,
    }
    return render(request, "travel.html", context)