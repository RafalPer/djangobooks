from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'date_published',
            'isbn',
            'number_of_pages',
            'link_to_cover',
            'language_of_publication',
        ]
        widgets = {
            'date_published': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
