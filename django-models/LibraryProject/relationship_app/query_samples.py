import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ---------------------------
# Create sample data (if not exists)
# ---------------------------
author_name = 'Author Name'
author, created = Author.objects.get_or_create(name=author_name)

book1, created = Book.objects.get_or_create(title='Book 1', author=author)
book2, created = Book.objects.get_or_create(title='Book 2', author=author)

library_name = 'Central Library'
library, created = Library.objects.get_or_create(name=library_name)
library.books.add(book1, book2)

librarian_name = 'John Doe'
librarian, created = Librarian.objects.get_or_create(name=librarian_name, library=library)

# ---------------------------
# 1. Query all books by a specific author
# ---------------------------
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print("Books by Author Name:")
for book in books_by_author:
    print(book.title)

# ---------------------------
# 2. List all books in a library
# ---------------------------
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# ---------------------------
# 3. Retrieve the librarian for a library
# ---------------------------
library = Library.objects.get(name=library_name)
librarian = library.librarian

print("\nLibrarian for Central Library:")
print(librarian.name)
