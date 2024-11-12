from django.test import TestCase
from intro_proj.models import User
from intro_proj.models import Post
from intro_proj.models import Comment

# Create your tests here.

class DatabaseTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_creation(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        user = User.objects.get(email='user@sandiego.edu')
        self.assertEqual('user@sandiego.edu', user.email)

    def test_post_creation(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        post = Post.objects.get(post_ID=test_post.post_ID)
        self.assertEqual('cool post', post.content)
    
    def test_comment_creation(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        test_comment = Comment.objects.create(author=test_user, parent_post=test_post, content='cool comment')
        comment = Comment.objects.get(comment_ID=test_comment.comment_ID)
        self.assertEqual('cool comment', comment.content)
    
    def test_post_cascade(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        post_id = test_post.post_ID
        test_user.delete()
        post_exists = Post.objects.filter(post_ID=post_id).exists()
        self.assertFalse(post_exists)
    
    def test_comment_post_cascade(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        test_comment = Comment.objects.create(author=test_user, parent_post=test_post, content='cool comment')
        comment_id = test_comment.comment_ID
        test_post.delete()
        comment_exists = Comment.objects.filter(comment_ID=comment_id).exists()
        self.assertFalse(comment_exists)
    
    def test_comment_user_cascade(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_user_2 = User.objects.create(email='user2@sandiego.edu', username='John User2')
        test_post = Post.objects.create(author=test_user, content='cool post')
        test_comment = Comment.objects.create(author=test_user_2, parent_post=test_post, content='cool comment')
        comment_id = test_comment.comment_ID
        test_user_2.delete()
        comment_exists = Comment.objects.filter(comment_ID=comment_id).exists()
        self.assertFalse(comment_exists)

    '''def test_user_duplicate_email(self):
        User.objects.create(email='user@sandiego.edu', username='John User')
        with self.assertRaises(Exception):
            User.objects.create(email='user@sandiego.edu', username='Another User')'''
    '''This test no longer passes due to the Django built-in User model not requiring unique emails.
    We will have to handle this during the registration process, since using the built-in User class
    saves a lot of headaches.
    This functionality is still tested in test_login.py.'''
    

    def test_post_timestamp(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        self.assertIsNotNone(test_post.time_posted)

    def test_comment_timestamp(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        test_comment = Comment.objects.create(author=test_user, parent_post=test_post, content='cool comment')
        self.assertIsNotNone(test_comment.time_posted)

    def test_multiple_comments_on_post(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        Comment.objects.create(author=test_user, parent_post=test_post, content='cool 1')
        Comment.objects.create(author=test_user, parent_post=test_post, content='cool 2')
        self.assertEqual(Comment.objects.filter(parent_post=test_post).count(), 2)

    def test_multi_comment_cascade(self):
        test_user = User.objects.create(email='user@sandiego.edu', username='John User')
        test_post = Post.objects.create(author=test_user, content='cool post')
        Comment.objects.create(author=test_user, parent_post=test_post, content='cool 1')
        Comment.objects.create(author=test_user, parent_post=test_post, content='cool 2')
        test_post_id = test_post.post_ID
        test_post.delete()
        self.assertEqual(Comment.objects.filter(parent_post=test_post_id).count(), 0)
