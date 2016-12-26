from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, mixins, permissions, viewsets, status
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

@method_decorator(csrf_exempt, name='dispatch')
class GameSearcher(View):

    http_method_names = ['post']
    
    def post(self, request, format=None):
        # Serialize "new" member's email
        serializer = serializers.SearchingPlayerSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        print("Player ID sent in: {}".format(serializer.player_id))
        return Response("Still working here, gimme a second",
                        status=status.HTTP_501_NOT_IMPLEMENTED)

