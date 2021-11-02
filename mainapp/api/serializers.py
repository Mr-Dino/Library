from rest_framework import serializers
from rest_framework.settings import api_settings

from ..models import *


class AuthorSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=250, min_length=None, allow_blank=False)
    first_name = serializers.CharField(max_length=255, required=True)
    surname = serializers.CharField(max_length=255, required=True)
    patronymic = serializers.CharField(max_length=255, required=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False, required=True)
    date_of_birth = serializers.DateField(format=api_settings.DATE_FORMAT, input_formats=None)

    class Meta:
        model = Author
        fields = ['id', 'slug', 'first_name', 'surname', 'patronymic', 'image', 'date_of_birth']


class GenreSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    slug = serializers.SlugField(max_length=250, min_length=None, allow_blank=False)

    class Meta:
        model = Genre
        fields = ['id', 'title', 'slug']


class AuthorForBooksSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, required=True)
    surname = serializers.CharField(max_length=255, required=True)
    patronymic = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Author
        fields = ['first_name', 'surname', 'patronymic']


class GenreForBooksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Genre
        fields = ['title']


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    slug = serializers.SlugField(max_length=250, min_length=None, allow_blank=False)
    author = AuthorForBooksSerializer()
    description = serializers.CharField(required=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False, required=True)
    issue_date = serializers.DateField(format=api_settings.DATE_FORMAT, input_formats=None)
    genre = GenreForBooksSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'slug', 'author', 'description', 'image', 'issue_date', 'genre']


