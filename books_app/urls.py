from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/add', views.add_from_api_view, name='add_api'),
    path('create/', views.book_create_view, name='create'),
    re_path(r'^edit/(?P<isbn>.+)/$', views.book_edit_view, name='edit'),
    path('date/search', views.date_search_view, name='date_search'),
    path('author/search', views.author_search_view, name='author_search'),
    path('title/search', views.title_search_view, name='title_search'),
    path('language/search', views.language_search_view, name='language_search'),

]
