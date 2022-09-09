from django.shortcuts import render
from katalog.models import CatalogItem


def show_catalog(request):
    data_catalog_items = CatalogItem.objects.all()
    context = {
        'catalog_item': data_catalog_items,
        'name': 'Aidah Novallia Putri',
        'npm': '2106653400'
    }
    return render(request, "katalog.html", context)
