from django.contrib import admin
from testapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate', 'moviename', 'hero', 'heroine', 'ratting']

admin.site.register(Movie, MovieAdmin)
