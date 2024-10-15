from django.utils.crypto import get_random_string
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
import logging

User = get_user_model()

logger = logging.getLogger(__name__)


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


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['costum_users_name', 'costum_users_email', 'password']

    def send_confirmation_code(self, user, confirmation_code):
        try:
            subject = 'Код подтверждения'
            message = f'Ваш код подтверждения: {confirmation_code}'
            from_email = settings.EMAIL_HOST_USER
            to_email = user.costum_users_email
            send_mail(subject, message, from_email, [
                      to_email], fail_silently=False)
        except Exception as e:
            logger.error(f"Error sending email: {e}")

    def create(self, validated_data):
        password = validated_data.pop('password')  # Извлекаем пароль
        user = super().create(validated_data)  # Создаем пользователя без пароля
        user.set_password(password)  # Устанавливаем зашифрованный пароль
        confirmation_code = get_random_string(
            length=6, allowed_chars='0123456789')
        user.confirmation_code = confirmation_code
        user.save()  # Сохраняем изменения пользователя
        # Отправка кода подтверждения
        self.send_confirmation_code(user, confirmation_code)
        return user


class ConfirmCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        user = CustomUser.objects.get(costum_users_email=email)
        if user.confirmation_code != data.get('confirmation_code'):
            raise serializers.ValidationError('Неправильный код подтверждения')
        return data

    def save(self, **kwargs):
        email = self.validated_data['email']
        user = CustomUser.objects.get(costum_users_email=email)
        user.is_active = True
        user.save()
        return user
