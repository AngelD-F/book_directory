from django.shortcuts import render, redirect, get_object_or_404

from book_directory.models import Book

from .models import Book
from .forms import BookForm
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


def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')

    ctx = {
        'form': form
    }
    return render(request, 'book_directory/book_form.html', ctx)


def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('../../')

    ctx = {
        'form': form,
        'book': book,
    }
    return render(request, 'book_directory/book_form.html', ctx)


def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('../../')

    ctx = {
        'book': book,
    }
    return render(request, 'book_directory/delete_book.html', ctx)
