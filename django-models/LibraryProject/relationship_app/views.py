from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # ✅ Import both models


# ✅ Function-based view: shows a list of all books and their authors
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ✅ Class-based view: shows details for a specific library, listing its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books for this specific library to the context
        context['books'] = Book.objects.filter(library=self.object)
        return context
