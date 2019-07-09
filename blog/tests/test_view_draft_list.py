from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.urls import resolve
from ..models import Post, Author
from .. import views

User = get_user_model()

class DraftListTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        author = Author.objects.create(user=user)
        self.client.login(username='john', password='123')
        Post.objects.create(title="Greeting", content="Hello, world!", author=author)
        url = reverse('blog:post_draft_list')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve("/mawazo/drafts/")
        self.assertEquals(view.func.view_class, views.DraftListView)
