from django.test import TestCase
from .. import models


class TestModels(TestCase):

    def test_should_create_book(self):
        book = models.Book.objects.create(
            title='Test Book',
            author='Test Author',
            date_published='2020-12-12',
            isbn='123456789',
            number_of_pages=999,
            link_to_cover='https://www.google.pl/',
            language_of_publication='en'
        )
        book.save()
        self.assertEqual(str(book), '123456789')
