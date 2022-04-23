from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "type", "time", 'added_at')
    list_display_links = ("id", 'title')


admin.site.register(News, NewsAdmin)
