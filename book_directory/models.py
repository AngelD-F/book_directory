from django.db import models

# Create your models here.
class Book(models.Model):
    book_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    year = models.DateField(null=True)

    def __str__(self):
        return self.title

class BookStore(models.Model):
    book = models.ForeignKey(Book)
    count = models.IntegerField(default=0)
