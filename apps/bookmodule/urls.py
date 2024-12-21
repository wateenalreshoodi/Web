from django.urls import path
from apps.bookmodule import views

urlpatterns = [
    # Static pages
    path('', views.index, name="books.index"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    # Book-specific views
    path('viewbook/<int:book_id>/', views.view_book, name="books.view_one_book"),
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),

    # HTML5 Demonstrations
    path('html5/links/', views.links, name="books.links"),
    path('html5/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),

    # Query views
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lookup/query/', views.lookup_query, name="books.lookup_query"),
    path('search/', views.search_books, name="books.search_books"),

    # Miscellaneous
    path('index2/<int:val1>/', views.index2, name="books.index2"),
    path('lab8/task1', views.task1_view, name='task1'),
    path('lab8/task2', views.task2_view, name='task2'),
    path('lab8/task3', views.task3_view, name='task3'),
    path('lab8/task4', views.task4_view, name='task4'),
    path('lab8/task5', views.task5_view, name='task5'),
    path('lab8/task6', views.task6_view, name='task6'),
    path('lab8/task7', views.task7_view, name='task7'),

    # Student views
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
]
