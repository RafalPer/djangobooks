from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, views.index)

    def test_api_url_resolves(self):
        url = reverse('add_api')
        self.assertEquals(resolve(url).func, views.add_from_api_view)

    def test_create_url_resolves(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, views.book_create_view)

    def test_edit_url_resolves(self):
        url = reverse('edit', args=['754734655234'])
        self.assertEquals(resolve(url).func, views.book_edit_view)

    def test_date_search_url_resolves(self):
        url = reverse('date_search')
        self.assertEquals(resolve(url).func, views.date_search_view)

    def test_author_search_url_resolves(self):
        url = reverse('author_search')
        self.assertEquals(resolve(url).func, views.author_search_view)

    def test_title_search_url_resolves(self):
        url = reverse('title_search')
        self.assertEquals(resolve(url).func, views.title_search_view)

    def test_language_search_url_resolves(self):
        url = reverse('language_search')
        self.assertEquals(resolve(url).func, views.language_search_view)
