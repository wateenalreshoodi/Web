from django.urls import path
from . import views

urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>/', views.viewbook),
 path('html5/links/', views.links_view, name='links'),
 path('html5/text/formatting/', views.formatting_view, name='formatting'),
 path('html5/listing/', views.listing_view, name='listing'),
 path('html5/tables/', views.tables_view, name='tables'),
]
