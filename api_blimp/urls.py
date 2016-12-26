__author__ = 'davidaxelrod'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^players/$', views.ListCreatePlayer.as_view(), name='player_list'),
    url(r'^games/$', views.CreateListGame.as_view(), name="list_games"),
    url(r'^game/(?P<game_pk>\d+)/$', views.GetUpdateGame.as_view(), name="single_game"),

]