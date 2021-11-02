from django.urls import path

from .api_views import *

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name="author_api"),
    path('genres/', GenreListAPIView.as_view(), name="genre_api"),
    path('books/', BookListAPIView.as_view(), name="book_api"),
    path('books/<str:title>/', BookDetailAPIView.as_view(), name="book_detail"),
]
