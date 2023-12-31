# Generated by Django 4.2.1 on 2023-06-17 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_type_movies_catalogue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='section',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.category'),
        ),
    ]
