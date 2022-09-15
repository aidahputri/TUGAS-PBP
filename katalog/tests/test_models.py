from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
  def setUp(self):
    CatalogItem.objects.create (
      item_name = "ipad",
      item_price = "8999999",
      item_stock = "17",
      description = "barang baru dari afrika",
      rating = "4",
      item_url = "https://www.apple.com/id/ipad/"
    )

  def test_catalog_models(self):
    ipad = CatalogItem.objects.get(item_name = "ipad")
    self.assertEquals(ipad.item_name, "ipad")
