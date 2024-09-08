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


class BooksSerializers(serializers.ModelSerializer):
    author_books = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = (
            'title_books',
            'author_books',
            'genre_books',
            'rating',
            'cover_image_path'
        )

    def get_author_books(self, obj):
        return obj.author_books.authors_full_name


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating']


class BooksDetailSerializers(serializers.ModelSerializer):
    author_books = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='authors_full_name'
    )
    genre_books = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='genres_name'
    )
    publisher_books = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='publishers_name'
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
