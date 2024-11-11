from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('subject', 'content')
    date_hierarchy = 'created_at'
