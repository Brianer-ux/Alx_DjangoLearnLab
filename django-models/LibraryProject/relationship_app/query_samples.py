import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. Query all books by a specific author
author = Author.objects.get(name='Author Name')
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
library = Library.objects.get(name='Library Name')
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# 3. Retrieve the librarian for a library
librarian = library.librarian  # One-to-one relationship
print(f"Librarian of {library.name}: {librarian.name}")
