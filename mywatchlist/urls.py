from django.urls import path
from mywatchlist.views import show_mywatchlist_html
from mywatchlist.views import show_mywatchlist_json
from mywatchlist.views import show_mywatchlist_xml
from mywatchlist.views import mywatchlist_home

app_name = 'mywatchlist'

urlpatterns = [
  path('', mywatchlist_home, name='mywatchlist_home'),
  path('html/', show_mywatchlist_html, name='mywatchlist_html'),
  path('json/', show_mywatchlist_json, name='mywatchlist_json'),
  path('xml/', show_mywatchlist_xml, name='mywatchlist_xml'),
]