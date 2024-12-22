from django.urls import path
from apps.bookmodule import views

# Static Pages
urlpatterns = [
     path('', views.index, name="books.index"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('index2/<int:val1>/', views.index2, name="books.index2"),
    
    # Book CRUD Operations
    path('viewbook/<int:book_id>/', views.view_book, name="books.view_one_book"),
    path('lab9_part1/listbooks/', views.list_books, name='lab9_part1.listbooks'),
    path('lab9_part1/addbook/', views.add_bookforms, name='lab9_part1.addbook'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='lab9_part1.editbook'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='lab9_part1.deletebook'),
    # Lab 8 Tasks
    path('lab8/task1/', views.task1_view, name='lab8.task1'),
    path('lab8/task2/', views.task2_view, name='lab8.task2'),
    path('lab8/task3/', views.task3_view, name='lab8.task3'),
    path('lab8/task4/', views.task4_view, name='lab8.task4'),
    path('lab8/task5/', views.task5_view, name='lab8.task5'),
    path('lab8/task6/', views.task6_view, name='lab8.task6'),
    path('lab8/task7/', views.task7_view, name='lab8.task7'),

    # HTML5 Demonstrations
    path('html5/links/', views.links, name="books.links"),
    path('html5/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),

    # Query Views
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lookup/query/', views.lookup_query, name="books.lookup_query"),
    path('search/', views.search_books, name="books.search"),

    # Student Views
    path('students/', views.list_students, name='students.list'),
    path('students/add/', views.add_student, name='students.add'),
    path('students/edit/<int:id>/', views.edit_student, name='students.edit'),
    path('students/delete/<int:id>/', views.delete_student, name='students.delete'),

    path('upload/', views.upload_image, name='upload_image'),
]
