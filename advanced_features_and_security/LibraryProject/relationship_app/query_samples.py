import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "John Doe"
author = Author.objects.get(name=author_name)  
books_by_author = Book.objects.filter(author=author)
print(f"\nBooks by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()

    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' does not exist.")

# 3. Retrieve the librarian of the library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\nNo librarian found for '{library_name}'.")
