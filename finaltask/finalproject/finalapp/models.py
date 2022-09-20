from django.db import models

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    servicecharge = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name