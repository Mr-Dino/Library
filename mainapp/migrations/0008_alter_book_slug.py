# Generated by Django 3.2.8 on 2021-10-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True, verbose_name='URL'),
        ),
    ]