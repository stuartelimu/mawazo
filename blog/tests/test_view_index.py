from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth import get_user_model
from .. import views
from ..models import Post, Author
from ..forms import PostForm

User = get_user_model()

class IndexTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/mawazo/')
        self.assertEquals(view.func.view_class, views.PostListView)









