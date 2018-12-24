from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        self.title #Title of the image
    
    class Meta:
        ordering = ["-timestamp"] #Ordering images from newest to oldest. remove negative sign for reversed