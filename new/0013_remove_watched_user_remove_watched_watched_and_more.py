# Generated by Django 4.2.1 on 2023-06-17 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watched',
            name='user',
        ),
        migrations.RemoveField(
            model_name='watched',
            name='watched',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='category',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Watched',
        ),
    ]
