from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_musician(request):
    if request.method == "POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = forms.MusicianForm()
    return render(request, 'musician.html', {'form':form})


def delete_musician(request, id):
    musician = models.Musician.objects.all()
    musician.delete()
    return redirect('home')