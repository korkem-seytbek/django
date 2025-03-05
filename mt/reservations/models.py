from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.date})"
