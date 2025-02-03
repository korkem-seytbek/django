from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)

# Create your models here.
