from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_code(user, confirmation_code):
    subject = 'Код подтверждения'
    message = f'Ваш код подтверждения: {confirmation_code}'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.costum_users_email
    send_mail(subject, message, from_email, [to_email], fail_silently=False)
