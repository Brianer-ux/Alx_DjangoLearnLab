from django.db import models

from django.db import models

# Author model holds the author's name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model linked to Author using ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        related_name='books',  # REQUIRED for nested serialization
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

