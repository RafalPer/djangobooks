from django.test import TestCase, Client
from django.urls import reverse
from .. import models


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.edit_url = reverse('edit', args=['12345'])
        self.add_api_url = reverse('add_api')
        self.create_url = reverse('create')
        self.book1 = models.Book.objects.create(
            title='TestTitle',
            author='TestAuthor',
            date_published='1990-12-12',
            isbn='12345',
            number_of_pages=1111,
            link_to_cover='https://google.com',
            language_of_publication='en'
        )

    def test_books_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_app/index.html')

    def test_books_edit_GET(self):
        response = self.client.get(self.edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_app/create.html')

    def test_add_api_GET(self):
        response = self.client.get(self.add_api_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_app/api.html')

    def test_books_create_GET(self):
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_app/create.html')
