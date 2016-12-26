from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers
import datetime

class ListCreatePlayer(generics.ListCreateAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class CreateListGame(generics.ListCreateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

class GetUpdateGame(generics.RetrieveUpdateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    lookup_url_kwarg = "game_pk"


