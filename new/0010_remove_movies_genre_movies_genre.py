# Generated by Django 4.2.1 on 2023-06-17 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_watched_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.genre'),
        ),
    ]