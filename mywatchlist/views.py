from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList


def show_mywatchlist_xml(req):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist), content_type="application/xml")


def show_mywatchlist_json(req):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist), content_type="application/json")


def show_mywatchlist_html(req):
    mywatchlist = MyWatchList.objects.all()

    watched_films = 0
    not_watched_films = 0
    for i in mywatchlist:
        if i.watched:
            watched_films += 1
        else:
            not_watched_films += 1

    context = {
        "name": "Aidah Novallia Putri",
        "npm": "2106653400",
        "watched": watched_films,
        "not_watched": not_watched_films,
        "watchlist": mywatchlist,
    }

    return render(req, "mywatchlist.html", context)


def mywatchlist_home(req):
    context = {
        "name": "Aidah Novallia Putri",
        "npm": "2106653400",
    }
    
    return render(req, "mywatchlist_home.html", context)
