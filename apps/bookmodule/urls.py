from django.urls import path
from apps.bookmodule import views

urlpatterns = [
    # Static pages
    path('', views.index, name="books.index"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('list/', views.list_books, name="books.list_books"),

    # Book-specific views
    path('viewbook/<int:bookId>/', views.viewbook, name="books.view_one_book"),

    # HTML5 Demonstrations
    path('html5/links/', views.links, name="books.links"),
    path('html5/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),

    # Query views
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lookup/query/', views.lookup_query, name="books.lookup_query"),

    # Search view
    path('search/', views.search_books, name="books.search_books"),

    # Miscellaneous
    path('index2/<int:val1>/', views.index2, name="books.index2"),
]
