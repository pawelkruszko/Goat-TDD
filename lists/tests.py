from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>To-Do list</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("<html>"))
