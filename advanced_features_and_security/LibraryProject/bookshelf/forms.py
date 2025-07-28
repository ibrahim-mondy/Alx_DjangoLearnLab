from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']  # عدل حسب Model بتاعك
class BookSearchForm(forms.Form):
    title = forms.CharField(required=False)
