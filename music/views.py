from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song

# Create your views here.
def home(request):
    albums = Album.objects.all()
    songs = Song.objects.all()
    context = {
        "albums" : albums,
        "songs" : songs
    }
    return render(request, "music/home.html", context)
