from django.shortcuts import render
from .models import *
# Create your views here.

from django.db.models import Q

def index(request):
    return render(request,"index.html")

def browse_index(request):
    movies = Movies.objects.all()
    context = {}
    search_movie = ""
    if request.GET.get("search_movie"):
        search_movie = request.GET.get("search_movie")
        movies = movies.filter(
            Q(name__icontains=search_movie) |
            Q(category__name__icontains=search_movie)
            # Q(genre__name__icontains=search_movie)
        )

    try:
        who = Watched.objects.get(user=request.user)
        watched = who.watched.all()
        context = {
            "movies":movies,
            "watched":watched,
            "search_movie": search_movie
        }


    except:
        context={
            "movies":movies,
            "search_movie": search_movie
        }

    return render(request,"browse-index.html",context)