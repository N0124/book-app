from datetime import datetime

from django import forms

from books.models import Book

YEARS = [year for year in range(datetime.now().year,
                                datetime.now().year-100,
                                -1)]


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'price', 'publish_date']
        widgets = {
            'publish_date': forms.SelectDateWidget(years=YEARS)
        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'price', 'publish_date']
        widgets = {
            'publish_date': forms.SelectDateWidget(years=YEARS)
        }