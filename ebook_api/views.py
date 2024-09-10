from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.


class BooksApiList(generics.ListAPIView):
    queryset = Books.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    serializer_class = BooksDetailSerializers


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
