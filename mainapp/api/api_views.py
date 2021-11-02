from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


from .serializers import *
from ..models import *


class BasePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('Количество объектов', self.page.paginator.count),
            ('Следующая старница', self.get_next_link()),
            ('Предыдущая страница', self.get_previous_link()),
            ('Данные', data),
        ]))


class BookPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('Количество объектов', self.page.paginator.count),
            ('Следующая старница', self.get_next_link()),
            ('Предыдущая страница', self.get_previous_link()),
            ('Данные', data),
        ]))


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id', 'surname']
    pagination_class = BasePagination


class GenreListAPIView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title']
    pagination_class = BasePagination


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title']
    pagination_class = BookPagination


class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'title'
