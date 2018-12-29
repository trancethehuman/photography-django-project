from django.shortcuts import render
from .models import Photo
# Create your views here.

def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos":queryset,
    }
    return render(request, "portraits.html", context)