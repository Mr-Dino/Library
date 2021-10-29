from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'issue_date')
    list_filter = ('title', 'author', 'genre')
    fields = ['title', 'slug', 'author', 'description', 'image', 'issue_date', 'genre']
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'patronymic', 'slug', 'date_of_birth')
    list_filter = ('surname', 'date_of_birth')
    fields = ['first_name', 'surname', 'patronymic', 'slug',  'image', 'date_of_birth']
    prepopulated_fields = {'slug': ('surname',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)