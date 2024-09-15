from rest_framework import serializers
from .models import *


class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = (
            'authors_first_name',
            'authors_last_name',
            'authors_full_name',
            'authors_slug',
        )


class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = (
            'genres_id',
            'genres_name',
            'genres_slug'
        )


class RatingSerializers(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        max_digits=2, decimal_places=1, coerce_to_string=False)

    class Meta:
        model = Rating
        fields = ['rating_id', 'what_book', 'rating']


class PublishersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ['publishers_name', 'publishers_slug', 'publishers_id']


class BooksDetailSerializers(serializers.ModelSerializer):
    author_books = AuthorsSerializers(read_only=True)
    genre_books = GenresSerializers(read_only=True)
    publisher_books = PublishersSerializers(
        many=False,
        read_only=True,
    )
    rate = RatingSerializers(many=True, read_only=True, source='book_rate')

    class Meta:
        model = Books
        fields = [
            'title_books',
            'author_books',
            'genre_books',
            'rate',
            'description_books',
            'cover_image_path',
            'link_to_file',
            'publication_date',
            'publisher_books',
            'available',
            'book_slug'
        ]
