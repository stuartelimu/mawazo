from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse
from ..views import SignUpView
from ..forms import SignUpForm

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('accounts:signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEquals(view.func.view_class, SignUpView)


class SignUpFormTests(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
