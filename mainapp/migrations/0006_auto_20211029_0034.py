# Generated by Django 3.2.8 on 2021-10-28 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_book_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='Если нет подходящего автора, добавьте его собственноручно', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Для того чтобы выбрать несеолько жанров, зажмите клавишу ctrl', to='mainapp.Genre', verbose_name='Жанр'),
        ),
    ]
