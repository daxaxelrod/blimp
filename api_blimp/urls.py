__author__ = 'davidaxelrod'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreatePlayer.as_view(), name='player_list'),

]