from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=255)
    postedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 