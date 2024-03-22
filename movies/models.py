from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
  title = models.CharField(max_length=255)
  src = models.CharField(max_length=255)
  genre = models.CharField(max_length=20)
  def __str__(self):
    return self.title

class Watchlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.movie.title} ({self.user.username})"

class Watched(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.movie.title} ({self.user.username})"

class Likes(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.movie.title} ({self.user.username})"