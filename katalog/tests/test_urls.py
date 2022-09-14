from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_catalog

class TestUrls(TestCase):
  def test_catalog_urls(self):
    url = reverse('katalog:show_catalog')
    self.assertEquals(resolve(url).func, show_catalog)