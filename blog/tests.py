from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):  # runs just ones
        cls.user = User.objects.create(
            username="testuser",
        )
        cls.post1 = Post.objects.create(
            title="post one",
            text="This is my first post",
            status=Post.STATUS_CHOICES[0][0],  # published
            author=cls.user,
        )

        cls.post2 = Post.objects.create(
            title="post two",
            text="this is my second post",
            status=Post.STATUS_CHOICES[1][0],  # draft
            author=cls.user,
        )

    # def setUp(self): -> runs for every method

    def test_post_list_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_list_url_by_name(self):
        rseponse = self.client.get(reverse("post_list"))

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f"/blog/{self.post1.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse("post_detail", args=[self.post1.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_on_blog_detail_page(self):
        response = self.client.get(reverse("post_detail", args=[self.post1.pk]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse("post_detail", args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_not_show_draft_posts(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)


class TemplateTest(TestCase):
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

    def test_blog_list_template(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "blog/posts_list.html")

    def test_blog_detail_template(self):
        response = self.client.get(reverse("post_detail", args=[self.post1.pk]))
        self.assertTemplateUsed(response, "blog/post_detail.html")
