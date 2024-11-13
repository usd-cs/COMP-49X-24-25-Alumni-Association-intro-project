from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_ID = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ['-time_posted']

class Comment(models.Model):
    comment_ID = models.AutoField(primary_key=True, unique=True) #auto-increments
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE) #auto-deletes the comment when the post is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.CharField(max_length=400)
    time_posted = models.DateTimeField(auto_now_add=True) #gets datetime when object is created

    def __str__(self):
        return f'Comment by {self.author.username} on {self.parent_post.content[:30]}'

    class Meta:
        ordering = ['-time_posted']