from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    genre = models.CharField(max_length = 255)
    is_archive = models.BooleanField(default=False)


class LogTable(models.Model):
    action_choice = [
        ('Create', 'Create'),
        ('Update', 'Update'),
        ('Delete', 'Delete')
    ]
    book_name = models.CharField(max_length=255)
    action = models.CharField(max_length=255, choices=action_choice)

