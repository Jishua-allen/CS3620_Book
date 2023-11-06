from django.db import models

# Create your models here.

class Book(models.Model):
  def __str__(self):
    return self.title

  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/')
  description = models.TextField()
  category = models.CharField(max_length=100, default='Uncategorized')
  rating = models.FloatField()