import random

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(sl):
    new_slug = slugify(sl, allow_unicode=True)
    return new_slug + '-' + str(random.randint(1, 1000))


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=250, db_index=True, blank=True, verbose_name="URL", unique=True,
                            help_text="Оставьте поле пустым, оно генерируется автоматически")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name="Автор",
                               help_text="Если нет подходящего автора, добавьте его собственноручно")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="books/%Y/%m/d", verbose_name="Изображение")
    issue_date = models.DateField(verbose_name="Дата выпуска", help_text="Формат: дд.мм.год")
    genre = models.ManyToManyField('Genre', verbose_name="Жанр", help_text="Для того чтобы выбрать несколько жанров, "
                                                                           "зажмите клавишу ctrl")

    def save(self, * args, **kwargs):
        if not self.pk:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_book', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['author', 'issue_date']
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Author(models.Model):
    slug = models.SlugField(max_length=250, db_index=True, blank=True, verbose_name="URL", unique=True,
                            help_text="Оставьте поле пустым, оно генерируется автоматически")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")
    image = models.ImageField(upload_to="author/%Y/%m/d", verbose_name="Изображение")
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    def save(self, * args, **kwargs):
        if not self.pk:
            self.slug = gen_slug(self.surname)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('author', kwargs={"author_id": self.pk})

    class Meta:
        ordering = ['surname']
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name="Жанр")
    slug = models.SlugField(max_length=250, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

