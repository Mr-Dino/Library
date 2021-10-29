from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', BooksView.as_view(), name="home"),
    path('filter/', FilterBooksView.as_view(), name="filter"),
    path('registration/', registration, name="registration"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('book/<slug:slug>/', ViewBook.as_view(), name="view_book"),
    path('authors/', cache_page(60) (AuthorsView.as_view()), name="authors"),
    path('library/add-book/', AddBook.as_view(), name="add_book"),
    path('library/add-author/', AddAuthor.as_view(), name="add_author"),
    path('author/<int:author_id>/', BooksByAuthor.as_view(), name="author"),

]
