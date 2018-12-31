from django.contrib import admin
from .models import PhotoTravel
# Register your models here.
class PhotoAdminTravel(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = PhotoTravel
    
admin.site.register(PhotoTravel, PhotoAdminTravel)