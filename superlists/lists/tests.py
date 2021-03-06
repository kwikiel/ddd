from django.core.urlresolvers import resolve
from django import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve ('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        
        self.assertTrue(response.content.startwith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.context.endswith(b'</html>'))



