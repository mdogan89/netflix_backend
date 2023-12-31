# Generated by Django 4.2.1 on 2023-06-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_category_remove_movies_section_delete_section_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Genre')),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='catalogue',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(to='movies.genre'),
        ),
    ]
