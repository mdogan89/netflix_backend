# Generated by Django 4.2.1 on 2023-06-17 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_category_genre_movies_category_movies_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Catalog',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='category',
            new_name='catalog',
        ),
    ]
