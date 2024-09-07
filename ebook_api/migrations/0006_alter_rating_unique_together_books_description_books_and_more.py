# Generated by Django 5.1 on 2024-09-07 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_api', '0005_alter_rating_book_alter_rating_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='books',
            name='description_books',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='what_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_rate', to='ebook_api.books'),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='book',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
