# Generated by Django 5.1 on 2024-09-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_api', '0002_alter_orders_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]