from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_album(request):
    if request.method == "POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = forms.AlbumForm()
    return render(request, 'musician.html', {'form':form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)

    if request.method == "POST":
        album_form=forms.AlbumForm(request.POST, instance=album )
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'album.html', {'form': album_form})
