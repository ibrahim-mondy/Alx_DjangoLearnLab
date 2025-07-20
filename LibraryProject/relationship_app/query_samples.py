import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian # type: ignore

# Query 1: Get all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# Query 2: List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Query 3: Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"Librarian at {library_name}: {librarian.name}")
