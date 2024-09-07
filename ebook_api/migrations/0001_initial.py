# Generated by Django 5.1 on 2024-09-05 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('authors_id', models.AutoField(primary_key=True, serialize=False)),
                ('authors_first_name', models.CharField(max_length=800)),
                ('authors_middle_name', models.CharField(blank=True, max_length=800, null=True)),
                ('authors_last_name', models.CharField(max_length=800)),
                ('authors_full_name', models.CharField(max_length=800)),
                ('authors_slug', models.SlugField()),
            ],
            options={
                'db_table': 'authors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CostumUsers',
            fields=[
                ('costum_users_id', models.AutoField(primary_key=True, serialize=False)),
                ('costum_users_name', models.CharField(max_length=800, unique=True)),
                ('costum_users_email', models.CharField(max_length=800, unique=True)),
                ('costum_users_password', models.CharField(max_length=800)),
                ('costum_users_password2', models.CharField(max_length=800)),
            ],
            options={
                'db_table': 'costum_users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genres_id', models.AutoField(primary_key=True, serialize=False)),
                ('genres_name', models.CharField(max_length=800)),
                ('genres_slug', models.SlugField()),
            ],
            options={
                'db_table': 'genres',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('publishers_id', models.AutoField(primary_key=True, serialize=False)),
                ('publishers_name', models.CharField(max_length=800)),
                ('publishers_slug', models.SlugField()),
            ],
            options={
                'db_table': 'publishers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('books_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_books', models.CharField(max_length=800)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('link_to_file', models.FilePathField(path='/www/ebook/media/all_books/')),
                ('cover_image_path', models.FilePathField(path='/www/ebook/media/cover_book/')),
                ('available', models.BooleanField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('book_slug', models.SlugField()),
                ('author_books', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_books', to='ebook_api.authors')),
                ('genre_books', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='genre_books', to='ebook_api.genres')),
                ('publisher_books', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='publisher_books', to='ebook_api.publishers')),
            ],
            options={
                'db_table': 'books',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orders_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ebook_api.books')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ebook_api.costumusers')),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
    ]
