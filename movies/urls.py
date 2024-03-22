from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('movies/', views.movies, name = 'movies'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('log_in/', views.log_in, name = 'log_in'),
    path('log_out/', views.log_out, name = 'log_out'),
    path('profile/', views.profile, name = 'profile'),
    path('watched/', views.watched, name = 'watched'),
    path('add_to_watched/<int:movie_id>/', views.add_to_watched, name='add_to_watched'),
    path('remove_from_watched/<int:movie_id>/', views.remove_from_watched, name='remove_from_watched'),
    path('watchlist/', views.watchlist, name = 'watchlist'),
    path('add_to_watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('likes/', views.likes, name = 'likes'),
    path('add_to_likes/<int:movie_id>/', views.add_to_likes, name='add_to_likes'),
    path('remove_from_likes/<int:movie_id>/', views.remove_from_likes, name='remove_from_likes'),
    path('test/', views.test, name = "test"),
]