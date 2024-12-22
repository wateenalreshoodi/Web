from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Address, Student
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import StudentForm, AddressForm, BookForm, ImageForm
from .models import ImageModel
# ---------------------------
# Static Pages
# ---------------------------
def index(request):
    return render(request, "bookmodule/index.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")


# ---------------------------
# Book Views
# ---------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_bookforms(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part1.listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book.html', {'form': form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part1.listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/editbook.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('lab9_part1.listbooks')
    return render(request, 'bookmodule/delete_book.html', {'book': book})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookmodule/one_book.html', {'book': book})
    return render(request, "bookmodule/one_book.html", {'book': book})


# ---------------------------
# HTML5 Demonstrations
# ---------------------------
def links(request):
    return render(request, "bookmodule/links.html")


def formatting(request):
    return render(request, "bookmodule/formatting.html")


def listing(request):
    return render(request, "bookmodule/listing.html")


def tables(request):
    return render(request, "bookmodule/tables.html")


# ---------------------------
# Query Views
# ---------------------------
def simple_query(request):
    books = Book.objects.filter(title__icontains='and')
    return render(request, "bookmodule/bookList.html", {'books': books})


def complex_query(request):
    books = Book.objects.filter(price__gt=20.0)
    return render(request, "bookmodule/bookList2.html", {'books': books})


def lookup_query(request):
    books = Book.objects.filter(
        Q(author__isnull=False),
        Q(title__icontains="and"),
        Q(edition__gte=2)
    ).exclude(price__lte=100)[:10]
    return render(request, "bookmodule/bookList.html", {'books': books})


# ---------------------------
# Search Books
# ---------------------------
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


# ---------------------------
# Lab 8 Task Views
# ---------------------------
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


# ---------------------------
# Student Views
# ---------------------------
def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save()
            return redirect('students.list')
    else:
        student_form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'student_form': student_form})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('students.list')
    else:
        student_form = StudentForm(instance=student)
    return render(request, 'bookmodule/edit_student.html', {'student_form': student_form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.addresses.clear()
        student.delete()
        return redirect('students.list')
    return render(request, 'bookmodule/delete_student.html', {'student': student})


# ---------------------------
# Image Upload
# ---------------------------
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm()
    
    images = ImageModel.objects.all()
    return render(request, 'bookmodule/upload_image.html', {'form': form, 'images': images})