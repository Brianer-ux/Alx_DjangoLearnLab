from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Updated ViewSet with authentication/permission
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Book model:
    list, create, retrieve, update, destroy
    Only authenticated users can access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Enforces that only logged-in users can access
