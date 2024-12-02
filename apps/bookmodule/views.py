from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Views for static pages
def index(request):
    return render(request, "bookmodule/index.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    # Example data for demonstration
    books = {
        123: {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
        456: {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'},
    }
    target_book = books.get(bookId)
    context = {'book': target_book}
    return render(request, "bookmodule/one_book.html", context)

# Views for HTML5 demonstrations
def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

# Views for queries
def simple_query(request):
    books = Book.objects.filter(title__icontains='and')
    return render(request, "bookmodule/bookList.html", {'books': books})

def complex_query(request):
    books = Book.objects.filter(price__gt=20.0)
    return render(request, "bookmodule/bookList2.html", {'books': books})

def lookup_query(request):
    books = Book.objects.filter(
        author__isnull=False,
        title__icontains="and",
        edition__gte=2
    ).exclude(price__lte=100)[:10]

    if books.exists():
        return render(request, "bookmodule/bookList.html", {'books': books})
    else:
        return render(request, "bookmodule/index.html")

# Search Books
def search_books(request):
    def __getBooksList():
        return [
            {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'},
            {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'},
            {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'},
        ]

    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_in_title = request.POST.get('option1')
        search_in_author = request.POST.get('option2')

        books = []
        for book in __getBooksList():
            if (search_in_title and keyword in book['title'].lower()) or \
               (search_in_author and keyword in book['author'].lower()):
                books.append(book)

        return render(request, "bookmodule/bookList.html", {'books': books})
    return render(request, "bookmodule/search.html")

# Miscellaneous views
def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")
