from django.db import models

class Book(models.Model):
    """
    Simple Book model for the first API.
    Fields:
      - title: short text for the book title
      - author: short text for author name
      - published_date: optional, when it was published
      - isbn: optional short code for ISBN
      - created_at: auto timestamp for creation
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']   # newest first by default
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} — {self.author}"
