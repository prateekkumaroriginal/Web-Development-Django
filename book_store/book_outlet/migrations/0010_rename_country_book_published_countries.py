# Generated by Django 4.2.2 on 2023-06-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_remove_country_published_books_book_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='country',
            new_name='published_countries',
        ),
    ]
