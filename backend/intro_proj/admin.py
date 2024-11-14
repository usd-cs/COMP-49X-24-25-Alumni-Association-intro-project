from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'time_posted')  
    list_filter = ('time_posted', 'author')
    search_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'parent_post', 'time_posted')
    list_filter = ('time_posted', 'author')
    search_fields = ('content',)