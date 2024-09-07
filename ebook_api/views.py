from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.


class BooksApiList(generics.ListAPIView):
    queryset = Books.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    serializer_class = BooksSerializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
