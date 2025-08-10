from django.db import models

# Create your models here.
# Author model:
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self, name):
        return self.name
    
# Book Model:
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Book')
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    