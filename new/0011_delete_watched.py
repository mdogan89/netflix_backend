# Generated by Django 4.2.1 on 2023-06-17 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_remove_movies_genre_movies_genre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watched',
        ),
    ]
