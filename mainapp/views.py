from django.contrib.auth import logout, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from .models import *
from .forms import *


class GenreAuthor:
    # Класс для вывода авторов и жанров
    def get_genres(self):
        return Genre.objects.all()

    def get_authors(self):
        return Author.objects.all()


class BooksView(GenreAuthor, ListView):
    # главная страница все книги
    model = Book
    template_name = "mainapp/home.html"
    context_object_name = 'books'
    paginate_by = 12
    allow_empty = False
    ordering = ["-issue_date"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Book.objects.all().prefetch_related('genre').select_related('author')


class ViewBook(DetailView):
    # детальное отображение книги
    model = Book
    context_object_name = "book"
    template_name = "mainapp/book_detail.html"


class AuthorsView(ListView):
    # отображение авторов
    model = Author
    template_name = "mainapp/authors.html"
    context_object_name = 'authors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторы'
        return context


class AddBook(CreateView):
    # добавление книги
    form_class = AddBookForm
    template_name = 'mainapp/add_book.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить книгу'
        return context


class AddAuthor(CreateView):
    # добавление автора
    form_class = AddAuthorForm
    template_name = 'mainapp/add_author.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить писателя'
        return context


class BooksByAuthor(ListView):
    # вывод книг по автору
    model = Book
    template_name = "mainapp/books_by_author.html"
    context_object_name = "books"
    paginate_by = 12
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = Author.objects.get(pk=self.kwargs['author_id'])
        return context

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_id'])


class FilterBooksView(GenreAuthor, ListView):
    template_name = "mainapp/home.html"
    context_object_name = 'books'
    paginate_by = 12
    ordering = ["-issue_date"]

    # фильтрация книг
    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(genre__in=self.request.GET.getlist('genre')) |
            Q(author__in=self.request.GET.getlist('author'))).select_related('author')
        return queryset.distinct()


def registration(request):
    # регистрация
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('home')
        else:
            messages.error(request, "Заполненная форма не прошла валидацию!")
    else:
        form = UserRegisterForm()
    return render(request, 'mainapp/registration.html', {"form": form})


def user_logout(request):
    # выход из аккаунта
    logout(request)
    return redirect('login')


def user_login(request):
    # авторизация
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Авторизация прошла успешно')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'mainapp/login.html', {'form': form})



