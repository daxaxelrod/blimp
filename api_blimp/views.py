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
