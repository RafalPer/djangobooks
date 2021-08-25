from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateField()
    isbn = models.CharField(max_length=200, primary_key=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    link_to_cover = models.TextField()
    language_of_publication = models.CharField(max_length=200)

    def __str__(self):
        return self.isbn
