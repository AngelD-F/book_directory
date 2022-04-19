from django.shortcuts import render

from book_directory.models import Book

from .models import Book
from .filters import BookFilter

# Create your views here.
def index(request):
    books = Book.objects.all()
    
    bookFilter = BookFilter(request.GET, queryset=Book.objects.all())

    ctx = {
        "books": books,
        "bookFilter": bookFilter,
    }

    return render(request, "book_directory/index.html", ctx)

