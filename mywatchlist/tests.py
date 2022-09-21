from urllib import response
from django.test import TestCase, Client
from django.urls import reverse

class TestUrl(TestCase):
    def test_url_html(self):
        client = Client()
        response = client.get("http://localhost:8000/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_xml(self):
        client = Client()
        response = client.get("http://localhost:8000/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_json(self):
        client = Client()
        response = client.get("http://localhost:8000/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)
