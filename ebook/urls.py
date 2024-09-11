"""
URL configuration for ebook_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ebook_api.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)
# router.register(r'genres', GenreViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/authors/', AuthorsViewList.as_view(), name='authors_list'),
    path('api/v1/authors/<slug:authors_slug>/',
         AuthorDetailView.as_view(), name='author_detail'),
    path('api/v1/authors/<slug:authors_slug>/books/',
         BooksByAuthorDetailView.as_view(), name='books_by_author_detail'),
    path('api/v1/genres/', GenresView.as_view(), name='genres_books_list'),
    path('api/v1/genres/<slug:genres_slug>/',
         GenreDetailView.as_view(), name='genre_detail'),
    path('api/v1/genres/<slug:genres_slug>/books/',
         BooksByGenreDetailView.as_view(), name='books_by_genre_detail'),
    path('api/v1/publishers/', PublishersViewList.as_view(), name='publishers_list'),
    path('api/v1/publishers/<slug:publishers_slug>/',
         PublisherDetailView.as_view(), name='publisher_detail'),
    path('api/v1/publishers/<slug:publishers_slug>/books/',
         BooksByPublisherDetailView.as_view(), name='books_by_publisher_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
