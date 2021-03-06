# Generated by Django 3.2.8 on 2021-10-27 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('image', models.ImageField(upload_to='author/%Y/%m/d', verbose_name='Изображение')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='books/%Y/%m/d', verbose_name='Изображение')),
                ('issue_date', models.DateTimeField(verbose_name='Дата выпуска')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.author', verbose_name='Жанр')),
                ('genre', models.ManyToManyField(to='mainapp.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
