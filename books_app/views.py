from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, BookSerializer
import requests

from .models import Book

from .forms import BookForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_fields = {
        'title': ['exact'],
        'author': ['exact'],
        'date_published': ['gte', 'lte'],
        'language_of_publication': ['exact'],
    }


def index(request):
    book_obj = Book.objects.all()
    context = {
        'book': book_obj,
    }
    return render(request, 'books_app/index.html', context)


def add_from_api_view(request):
    if 'q' in request.GET:
        search_term = request.GET['q']
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={search_term}'
        response = requests.get(api_url)
        data = response.json()
        result = {}
        for x in data['items']:
            # Creating Title and subtitle if present in api
            try:
                result['title'] = f"{x['volumeInfo']['title']}. {x['volumeInfo']['subtitle']}"
            except KeyError:
                result['title'] = x['volumeInfo']['title']
            # Creating Author if is present in api
            try:
                result['author'] = x['volumeInfo']['authors'][0]
            except KeyError:
                result['author'] = ''
            # Creating Date of Publication if present in api
            try:
                result['date_published'] = x['volumeInfo']['publishedDate']
                # Converting Year to Full Date
                if len(x['volumeInfo']['publishedDate']) == 4:
                    result['date_published'] = f"{x['volumeInfo']['publishedDate']}-01-01"
                # Converting Year and Month to Full Date
                if len(x['volumeInfo']['publishedDate']) == 7:
                    result['date_published'] = f"{x['volumeInfo']['publishedDate']}-01"
            except KeyError:
                result['date_published'] = ''
            # Creating ISBN
            result['isbn'] = x['volumeInfo']['industryIdentifiers'][0]['identifier']
            # Creating Number Of Pages
            try:
                result['number_of_pages'] = x['volumeInfo']['pageCount']
            except KeyError:
                result['number_of_pages'] = None
            # Creating Link To Cover
            try:
                result['link_to_cover'] = x['volumeInfo']['imageLinks']['thumbnail']
            except KeyError:
                result['link_to_cover'] = ''
            # Creating Language
            try:
                result['language_of_publication'] = x['volumeInfo']['language']
            except KeyError:
                result['language_of_publication'] = ''
            model = Book(**result)
            model.save()
        return redirect('index')
    return render(request, 'books_app/api.html')


def book_create_view(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = BookForm()
    context = {
        'form': form,
    }
    return render(request, 'books_app/create.html', context)


def book_edit_view(request, isbn):
    instance = get_object_or_404(Book, isbn=isbn)
    form = BookForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'books_app/create.html', {'form': form})


def date_search_view(request):
    if request.method == 'POST':
        from_date = request.POST.get('fromdate')
        to_date = request.POST.get('todate')
        search_result = Book.objects.filter(date_published__gte=from_date, date_published__lte=to_date)
        context = {
            'book': search_result,
        }
        return render(request, 'books_app/date.html', context)
    else:
        return render(request, 'books_app/date.html')


def author_search_view(request):
    if request.method == 'GET':
        author = request.GET.get('q')
        if not author:
            author = ''
        author_search = Book.objects.filter(author=author)
        context = {
                'book': author_search
        }
        return render(request, 'books_app/author.html', context)
    else:
        return render(request, 'books_app/author.html')


def title_search_view(request):
    if request.method == 'GET':
        title = request.GET.get('qtitle')
        if not title:
            title = ''
        title_search = Book.objects.filter(title=title)
        context = {
                'book': title_search
        }
        return render(request, 'books_app/title.html', context)
    else:
        return render(request, 'books_app/title.html')


def language_search_view(request):
    if request.method == 'GET':
        language = request.GET.get('qlanguage')
        if not language:
            language = ''
        language_search = Book.objects.filter(language_of_publication=language)
        context = {
                'book': language_search
        }
        return render(request, 'books_app/language.html', context)
    else:
        return render(request, 'books_app/language.html')
