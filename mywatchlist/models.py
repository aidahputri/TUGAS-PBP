from django.db import models

# Create your models here.
class MyWatchList(models.Model):
  watched = models.BooleanField()
  title = models.CharField(max_length=255)
  rating = models.IntegerField()
  release_date = models.DateField()
  review = models.CharField(max_length=255)
