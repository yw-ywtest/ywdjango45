# Generated by Django 5.1.1 on 2024-09-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_alter_movie_options_alter_movie_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.TextField(max_length=250, verbose_name="电影简介"),
        ),
    ]
