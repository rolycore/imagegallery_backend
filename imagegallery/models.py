from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
