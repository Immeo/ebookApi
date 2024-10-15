# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to createTruemodify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import os
from django.core.files.storage import default_storage


def book_path_local(instance, filename):
    # Путь, куда будет сохранен файл
    path = f'books/{instance.book_slug}/{filename}'

    # Проверяем, существует ли файл
    if default_storage.exists(path):
        # Если файл существует, возвращаем существующий путь
        return path
    else:
        # Если файла нет, возвращаем новый путь
        return path


class Authors(models.Model):
    authors_id = models.AutoField(primary_key=True)
    authors_first_name = models.CharField(max_length=800)
    authors_middle_name = models.CharField(
        max_length=800, blank=True, null=True)
    authors_last_name = models.CharField(max_length=800)
    authors_full_name = models.CharField(max_length=800)
    authors_slug = models.SlugField()

    def __str__(self):
        return self.authors_full_name

    class Meta:
        managed = True
        db_table = 'authors'


class Books(models.Model):
    books_id = models.AutoField(primary_key=True)
    title_books = models.CharField(max_length=800)
    description_books = models.TextField(blank=True, null=True)
    author_books = models.ForeignKey(
        Authors, models.DO_NOTHING, blank=True, null=True, related_name='author_books')
    genre_books = models.ForeignKey(
        'Genres', models.DO_NOTHING, blank=True, null=True, related_name='genre_books')
    publication_date = models.DateField(blank=True, null=True)
    publisher_books = models.ForeignKey(
        'Publishers', models.DO_NOTHING, blank=True, null=True, related_name='publisher_books')
    link_to_file = models.FileField(
        upload_to=book_path_local, blank=True, null=True, max_length=900)
    cover_image_path = models.FileField(
        upload_to=book_path_local, blank=True, null=True, max_length=900)
    available = models.BooleanField(blank=True, null=True)
    book_slug = models.SlugField()

    def __str__(self):
        return self.title_books

    def average_rating(self):
        ratings = Rating.objects.filter(
            book=self).values_list('rating', flat=True)
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

    class Meta:
        managed = True
        db_table = 'books'


class CustomUserManager(BaseUserManager):
    def create_user(self, costum_users_name, costum_users_email, password=None):
        if not costum_users_name:
            raise ValueError('Users must have a name')
        if not costum_users_email:
            raise ValueError('Users must have an email')

        if costum_users_email:
            costum_users_email = self.normalize_email(costum_users_email)

        user = self.model(
            costum_users_name=costum_users_name,
            costum_users_email=self.normalize_email(costum_users_email),
            confirmation_code=None,  # Добавлено поле confirmation_code
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, costum_users_name, costum_users_email, password):
        user = self.create_user(
            costum_users_name,
            costum_users_email,
            password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    costum_users_id = models.AutoField(primary_key=True)
    costum_users_name = models.CharField(unique=True, max_length=800)
    costum_users_email = models.EmailField(unique=True, max_length=800)
    costum_users_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    # Пользователь не активен по умолчанию
    is_active = models.BooleanField(default=False)
    # Добавлено поле confirmation_code
    confirmation_code = models.CharField(max_length=6, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'costum_users_name'
    REQUIRED_FIELDS = ['costum_users_email']

    objects = CustomUserManager()

    class Meta:
        managed = True
        db_table = 'costum_users'

    def __str__(self):
        return self.costum_users_name


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    what_book = models.ForeignKey(
        Books, on_delete=models.CASCADE, blank=True, null=True, related_name='book_rate')
    who_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='user_rate')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=1)

    class Meta:
        managed = True
        db_table = 'rating'

    def clean(self):
        if self.rating < 0 or self.rating > 5:
            raise ValidationError('Rating must be between 0 and 5')

    def __str__(self):
        return f'{self.what_book.title_books}'


class Genres(models.Model):
    genres_id = models.AutoField(primary_key=True)
    genres_name = models.CharField(max_length=800)
    genres_slug = models.SlugField()

    def __str__(self):
        return self.genres_name

    class Meta:
        managed = True
        db_table = 'genres'


class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, models.DO_NOTHING, blank=True, null=True, related_name='user_orders')
    book = models.ManyToManyField(
        Books, blank=True, related_name='book_orders')
    order_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.costum_users_name

    class Meta:
        managed = True
        db_table = 'orders'


class Publishers(models.Model):
    publishers_id = models.AutoField(primary_key=True)
    publishers_name = models.CharField(max_length=800)
    publishers_slug = models.SlugField()

    def __str__(self):
        return self.publishers_name

    class Meta:
        managed = True
        db_table = 'publishers'
