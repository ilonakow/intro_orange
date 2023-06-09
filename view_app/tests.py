from django.test import SimpleTestCase
from django.urls import resolve, reverse
from view_app import hello_function_view, HelloClassView
# Testowanie w Django
# - testowanie urls
# - testować widoki
# - testować modele
# - testować formularze

# testowanie urls
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_hello_template_url(self):
        url = reverse('view_app:hello_template')
        resolver = resolve(url)
        # print(resolver) # zawiera func, url_name, app_name, namespace, route, args i kwargs
        view = resolve(url.func)
        #assert resolver.func == hello_function_view
        self.assertEqual(view, hello_function_view)

    def test_hello_template2_url(self):
        url = reverse('view_app:hello_template2')
        view = resolve(url).func.view_class

        self.assertEqual(HelloClassView)
