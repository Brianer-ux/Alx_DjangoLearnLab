from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books from the database
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Book model:
    list, create, retrieve, update, destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer