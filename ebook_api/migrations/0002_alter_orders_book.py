# Generated by Django 5.1 on 2024-09-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='book',
            field=models.ManyToManyField(blank=True, related_name='book_orders', to='ebook_api.books'),
        ),
    ]
