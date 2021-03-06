# Generated by Django 3.2.8 on 2021-10-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, help_text='Оставьте поле пустым, оно генерируется автоматически', max_length=250, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, help_text='Оставьте поле пустым, оно генерируется автоматически', max_length=250, unique=True, verbose_name='URL'),
        ),
    ]
