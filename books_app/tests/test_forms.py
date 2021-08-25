from django.test import TestCase
from .. import forms


class TestForms(TestCase):

    def test_book_form_with_valid_data(self):
        form = forms.BookForm(data={
            'title': 'Test Title',
            'author': 'Test Author',
            'date_published': '1996-07-29',
            'isbn': '123456789',
            'number_of_pages': 999,
            'link_to_cover': 'https://google.com',
            'language_of_publication': 'en'
        })

        self.assertTrue(form.is_valid())

    def test_book_form_with_invalid_data(self):
        form = forms.BookForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)
