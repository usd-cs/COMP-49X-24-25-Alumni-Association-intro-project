from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from intro_proj.models import Post, Comment

class PostTests(TestCase):
    def setUp(self):
        # Create test user
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create test post
        self.post = Post.objects.create(
            author=self.user,
            content='Test post content'
        )
        # Create test comment
        self.comment = Comment.objects.create(
            parent_post=self.post,
            author=self.user,
            content='Test comment'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')  # Updated template path
        self.assertContains(response, 'Test post content')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'post_id': self.post.post_ID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')  # Updated template path
        self.assertContains(response, 'Test post content')
        self.assertContains(response, 'Test comment')

    def test_create_post_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('create_post'), {
            'content': 'New test post'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Post.objects.filter(content='New test post').exists())

    def test_create_post_unauthenticated(self):
        response = self.client.post(reverse('create_post'), {
            'content': 'New test post'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertFalse(Post.objects.filter(content='New test post').exists())

    def test_add_comment_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('add_comment', kwargs={'post_id': self.post.post_ID}),
            {'content': 'New test comment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Comment.objects.filter(content='New test comment').exists())

    def test_add_comment_unauthenticated(self):
        response = self.client.post(
            reverse('add_comment', kwargs={'post_id': self.post.post_ID}),
            {'content': 'New test comment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertFalse(Comment.objects.filter(content='New test comment').exists())

    def test_delete_comment_authorized(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('delete_comment', kwargs={'comment_id': self.comment.comment_ID})
        )
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(Comment.objects.filter(comment_ID=self.comment.comment_ID).exists())


    def test_delete_comment_unauthorized(self):
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )
        self.client.login(username='otheruser', password='otherpass123')
        response = self.client.get(
            reverse('delete_comment', kwargs={'comment_id': self.comment.comment_ID})
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(Comment.objects.filter(comment_ID=self.comment.comment_ID).exists())

    def test_post_model_str(self):
        self.assertEqual(str(self.post), self.post.content[:50])

    def test_comment_model_str(self):
        expected = f'Comment by {self.user.username} on {self.post.content[:30]}'
        self.assertEqual(str(self.comment), expected)

    def test_post_ordering(self):
        new_post = Post.objects.create(
            author=self.user,
            content='Newer post content'
        )
        posts = Post.objects.all()
        self.assertEqual(posts.first(), new_post)  # Newest should be first

    def test_comment_ordering(self):
        new_comment = Comment.objects.create(
            parent_post=self.post,
            author=self.user,
            content='Newer comment'
        )
        comments = Comment.objects.all()
        self.assertEqual(comments.first(), new_comment)  # Newest should be first
