from django.db import models

# Create your models here.

# model Author
class Author(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
# model Book
class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )