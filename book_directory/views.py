from django.shortcuts import render

from book_directory.models import Book

from .models import Book
from .filters import BookFilter

# Create your views here.
def index(request):
    # The books most be ordered by the book number by default
    # The first five
    books = Book.objects.all().order_by('book_number')

    bookFilter = BookFilter(request.GET, queryset=Book.objects.all())
    paginationNeeded = True

    ctx = {
        'books': books,
        'bookFilter': bookFilter,
        'paginationNeeded': paginationNeeded
    }

    return render(request, 'book_directory/index.html', ctx)

