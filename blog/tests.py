from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

class BlogPostTest(TestCase):
    def setUp(self):

        self.user = User.objects.create(
            username="testuser",
        )
        self.post1 = Post.objects.create(
            title="post one",
            text="This is my first post",
            status=Post.STATUS_CHOICES[0],
            author=self.user,
        )
        
    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
            
            
    def test_list_url_by_name(self):
        rseponse = self.client.get(reverse('post_list'))
        