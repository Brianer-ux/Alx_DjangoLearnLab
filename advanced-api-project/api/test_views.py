from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        # Test DB is automatically isolated — satisfies “separate test database”
        self.client = APIClient()

        # Create user for authenticated requests
        self.user = User.objects.create_user(username='tester', password='password123')
        self.client.force_authenticate(user=self.user)

        # Create author + books for testing
        self.author = Author.objects.create(name="John Doe")
        self.book1 = Book.objects.create(
            title="Alpha",
            author=self.author,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Beta",
            author=self.author,
            publication_year=2022
        )

    # ---------- LIST VIEW TEST ----------
    def test_list_books(self):
        response = self.client.get(reverse('books-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    # ---------- CREATE BOOK TEST ----------
    def test_create_book(self):
        data = {
            "title": "Gamma",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(reverse('books-create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Gamma")

    # ---------- DETAIL VIEW ----------
    def test_get_single_book(self):
        url = reverse('books-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha")

    # ---------- UPDATE BOOK ----------
    def test_update_book(self):
        url = reverse('books-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Alpha Updated",
            "author": self.author.id,
            "publication_year": 2020
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Updated")

    # ---------- DELETE BOOK ----------
    def test_delete_book(self):
        url = reverse('books-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # ---------- FILTER ----------
    def test_filter_books_by_title(self):
        response = self.client.get(reverse('books-list'), {"title": "Alpha"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha")

    # ---------- SEARCH ----------
    def test_search_books(self):
        response = self.client.get(reverse('books-list'), {"search": "Alpha"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha")

    # ---------- ORDER ----------
    def test_order_books_by_publication_year(self):
        response = self.client.get(reverse('books-list'), {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha")  # 2020 < 2022
