# myapp/middleware.py
from django.http import HttpResponse


class FrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # или 'SAMEORIGIN' если нужно ограничить
        response['X-Frame-Options'] = 'ALLOW-FROM *'
        return response
