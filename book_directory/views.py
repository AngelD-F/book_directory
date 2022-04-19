from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Lower

from .models import Book
from .forms import BookForm
from .filters import BookFilter

class PaginationContext:
    def __init__(self, items, page=1, items_per_page=10):
        self.items = items
        self.page = page
        self.items_per_page = items_per_page
        self.previous = self.page - 1
        self.is_previous = self.previous >= 1 
        self.next = self.page + 1
        self.is_next = self.items_per_page*self.page < self.items.count() 
        self.pages = range(1, self.items.count() % self.items_per_page)
    
    def get_items(self):
        return self.items[self.items_per_page*(self.page-1) : self.items_per_page*self.page]


def index(request):
    # The books most be ordered by the book number by default
    orderby = request.GET.get('orderby', 'book_number')
    page = int(request.GET.get('p', 1))

    # Process data
    books = Book.objects.all()
    book_count = books.count()
    bookFilter = BookFilter(request.GET, queryset=books)

    books = bookFilter.qs
    books = books.order_by(Lower(orderby))

    # Pagination
    pagination = PaginationContext(books, page)
    books = pagination.get_items()

    ctx = {
        'books': books,
        'book_count': book_count,
        'bookFilter': bookFilter,
        'pagination': pagination,
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
