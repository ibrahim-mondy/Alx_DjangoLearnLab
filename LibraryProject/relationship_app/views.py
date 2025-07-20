from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
from .models import Book

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
