# Generated by Django 4.2.1 on 2023-06-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watched',
            name='watched',
            field=models.ManyToManyField(null=True, to='movies.movies'),
        ),
    ]
