from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=15) 
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Achievements(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile_images", blank=True, null=True)
    description = models.CharField(max_length=1000)
    date = models.DateField(null=True, blank=True)  # Changed field name to match 'date'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ''
