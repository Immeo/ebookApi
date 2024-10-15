from django.contrib import admin
from .models import *

# Register your models here.


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["authors_full_name", "authors_slug"]
    prepopulated_fields = {"authors_slug": ("authors_full_name",)}


admin.site.register(Authors, AuthorsAdmin)


class GenresAdmin(admin.ModelAdmin):
    list_display = ["genres_name", "genres_slug"]
    prepopulated_fields = {"genres_slug": ("genres_name",)}


admin.site.register(Genres, GenresAdmin)


class PublishersAdmin(admin.ModelAdmin):
    list_display = ["publishers_name", "publishers_slug"]
    prepopulated_fields = {"publishers_slug": ("publishers_name",)}


admin.site.register(Publishers, PublishersAdmin)


class BooksAdmin(admin.ModelAdmin):
    list_display = ["title_books", "author_books", "link_to_file"]
    prepopulated_fields = {"book_slug": ("title_books",)}


admin.site.register(Books, BooksAdmin)

admin.site.register(Rating)

admin.site.register(CustomUser)
