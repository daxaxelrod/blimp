__author__ = 'davidaxelrod'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^players/$', views.ListCreatePlayer.as_view(), name='player_list'),
    url(r'^games/$', views.CreateListGame.as_view(), name="list_games"), # <- not useful so far
    url(r'^game/(?P<game_pk>\d+)/$', views.GetGame.as_view(), name="single_game"),
    url(r'^game/(?P<game_pk>\d+)/update/$', views.UpdateGame, name="update_single_game"),
    url(r'^game/(?P<game_pk>\d+)/projectile/(?P<player_pk>\d+)/$', views.CreateProjectile, name="create_projectile"),
    url(r'^game/(?P<game_pk>\d+)/new_projectiles/(?P<player_pk>\d+)/$', views.ListUnusedProjectiles, name="list_projectiles"),


    url(r'^searching/', views.GameSearcher, name="searching_for_a_game"),

]