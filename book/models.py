from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    #image ="ImageField"
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title
