from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_ID = models.AutoField(primary_key=True, unique=True) #auto-increments
    author = models.ForeignKey(User, on_delete=models.CASCADE) #auto-deletes the post when the author is deleted
    content = models.CharField(max_length=400)
    time_posted = models.DateTimeField(auto_now_add=True) #gets datetime when object is created

class Comment(models.Model):
    comment_ID = models.AutoField(primary_key=True, unique=True) #auto-increments
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE) #auto-deletes the comment when the post is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.CharField(max_length=400)
    time_posted = models.DateTimeField(auto_now_add=True) #gets datetime when object is created