# Generated by Django 3.2.8 on 2021-10-27 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211027_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author', 'issue_date'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
