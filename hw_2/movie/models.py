from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()  # Фильмнің ұзақтығы (секунд)

# Create your models here.
