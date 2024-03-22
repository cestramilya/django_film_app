from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def movies(request):
    myRomanceMovies = Movie.objects.filter(genre = "Romance").values()
    myHorrorMovies = Movie.objects.filter(genre = "Horror").values()
    myComedyMovies = Movie.objects.filter(genre = "Comedy").values()
    myActionMovies = Movie.objects.filter(genre = "Action").values()
    mymovies = Movie.objects.all().values()

    context = {
        'myRomanceMovies': myRomanceMovies,
        'myHorrorMovies' : myHorrorMovies,
        'myComedyMovies' : myComedyMovies,
        'myActionMovies' : myActionMovies,
        'mymovies' : mymovies,
    }

    return render(request, 'movies.html', context)

def main(request):
    return render(request, 'main.html')

def sign_up(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'sign_up.html', context)

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('movies')

    return render(request, 'log_in.html', {})

def log_out(request):
    logout(request)
    return redirect('main')

def profile(request):
    return render(request, 'profile.html', {})

def test(request):
    return render(request, 'test.html', {})

def watched(request):
    watched = Watched.objects.filter(user=request.user)
    context = {'watched': watched}
    return render(request, 'watched.html', context)

def add_to_watched(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    watched, created = Watched.objects.get_or_create(user=request.user, movie=movie)
    return redirect('watched')

def remove_from_watched(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    watched = Watched.objects.filter(user=request.user, movie=movie)
    watched.delete()
    return redirect('watched')

def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    context = {'watchlist': watchlist}
    return render(request, 'watchlist.html', context)

def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)
    return redirect('watchlist')

def remove_from_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    watchlist = Watchlist.objects.filter(user=request.user, movie=movie)
    watchlist.delete()
    return redirect('watchlist')

def likes(request):
    likes = Likes.objects.filter(user=request.user)
    context = {'likes': likes}
    return render(request, 'likes.html', context)

def add_to_likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    likes, created = Likes.objects.get_or_create(user=request.user, movie=movie)
    return redirect('likes')

def remove_from_likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    likes = Likes.objects.filter(user=request.user, movie=movie)
    likes.delete()
    return redirect('likes')