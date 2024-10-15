from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
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
    lookup_field = 'book_slug'

    @action(detail=False, methods=['get'], url_path='<slug:book_slug>')
    def get_by_slug(self, request, book_slug):
        try:
            book = Books.objects.get(book_slug=book_slug)
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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


class CustomUserCreateView(views.APIView):
    serializer_class = CustomUserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': 'Пользователь создан'}, status=status.HTTP_201_CREATED)


class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Successfully logged out'}, status=200)


class ConfirmCodeView(views.APIView):
    serializer_class = ConfirmCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')  # Добавьте поле email в сериализатор
        user = CustomUser.objects.get(costum_users_email=email)
        if user.confirmation_code != serializer.validated_data['confirmation_code']:
            raise serializers.ValidationError('Неправильный код подтверждения')
        user.is_active = True
        user.save()
        return Response({'message': 'Аккаунт успешно активирован'}, status=status.HTTP_200_OK)


class UserInfoView(views.APIView):
    permission_classes = [IsAuthenticated]  # Требует аутентификации

    def get(self, request):
        user = request.user  # Получаем текущего аутентифицированного пользователя

        # Возвращаем полезную информацию о пользователе согласно вашей модели
        user_info = {
            'costum_users_name': user.costum_users_name,
            'costum_users_email': user.costum_users_email,
            'costum_users_balance': user.costum_users_balance,
            'is_active': user.is_active,
        }

        return Response(user_info)
