
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Address, Student
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import StudentForm, AddressForm
# Static pages
def index(request):
    return render(request, "bookmodule/index.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

# Miscellaneous
def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")

# Book-specific views
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')

    return render(request, 'bookmodule/addbook.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('list_books')

    return render(request, 'bookmodule/editbook.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')

def view_book(request, book_id):
    books = {
        123: {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
        456: {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'},
    }
    target_book = books.get(book_id)
    if not target_book:
        return HttpResponse("Book not found", status=404)
    return render(request, "bookmodule/one_book.html", {'book': target_book})

# HTML5 Demonstrations
def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

# Query Views
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
    return render(request, "bookmodule/bookList.html", {'books': books})

# Search Books
def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_in_title = request.POST.get('option1')
        search_in_author = request.POST.get('option2')

        books = Book.objects.filter(
            Q(title__icontains=keyword) if search_in_title else Q(),
            Q(author__icontains=keyword) if search_in_author else Q(),
        )
        return render(request, "bookmodule/bookList.html", {'books': books})
    return render(request, "bookmodule/search.html")

# Lab 8 Task Views
def task1_view(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
    books = Book.objects.exclude(
        Q(edition__gt=2) | Q(title__icontains='qu') | Q(author__icontains='qu')
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task6_view(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task6.html', {'cities': cities})

def task7_view(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})


# List all students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        address_form = AddressForm(request.POST)
        if student_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            student = student_form.save(commit=False)
            student.address = address
            student.save()
            return redirect('list_students')
    else:
        student_form = StudentForm()
        address_form = AddressForm()
    return render(request, 'students/add_student.html', {'student_form': student_form, 'address_form': address_form})

# Edit an existing student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    address = student.address
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        address_form = AddressForm(request.POST, instance=address)
        if student_form.is_valid() and address_form.is_valid():
            address_form.save()
            student_form.save()
            return redirect('list_students')
    else:
        student_form = StudentForm(instance=student)
        address_form = AddressForm(instance=address)
    return render(request, 'students/edit_student.html', {'student_form': student_form, 'address_form': address_form})

# Delete a student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.address.delete()
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete_student.html', {'student': student})