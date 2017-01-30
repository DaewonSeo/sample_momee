from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()


    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
