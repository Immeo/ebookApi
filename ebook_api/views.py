from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.


class AuthorsViewList(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializers


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializers
    lookup_field = 'authors_slug'


class BooksByAuthorDetailView(generics.ListAPIView):
    serializer_class = BooksDetailSerializers

    def get_queryset(self):
        author_slug = self.kwargs['authors_slug']
        return Books.objects.filter(author_books__authors_slug=author_slug)


class PublishersViewList(generics.ListAPIView):
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializers


class PublisherDetailView(generics.RetrieveAPIView):
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializers
    lookup_field = 'publishers_slug'


class BooksByPublisherDetailView(generics.ListAPIView):
    serializer_class = BooksDetailSerializers

    def get_queryset(self):
        publisher_slug = self.kwargs['publishers_slug']
        return Books.objects.filter(publisher_books__publishers_slug=publisher_slug)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializers


class GenresView(generics.ListAPIView):
    serializer_class = GenresSerializers
    queryset = Genres.objects.all()


class GenreDetailView(generics.RetrieveAPIView):
    serializer_class = GenresSerializers
    queryset = Genres.objects.all()
    lookup_field = 'genres_slug'


class BooksByGenreDetailView(generics.ListAPIView):
    serializer_class = BooksDetailSerializers

    def get_queryset(self):
        genre_slug = self.kwargs['genres_slug']
        return Books.objects.filter(genre_books__genres_slug=genre_slug)
