from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for Book model.
# It exposes all fields of the Book model and performs
# validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


# Serializer for Author model.
# Includes a nested representation of books using BookSerializer.
# The 'books' field pulls related books using the related_name
# defined in the Book model's ForeignKey.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
