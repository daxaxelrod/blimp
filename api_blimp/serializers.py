__author__ = 'davidaxelrod'
from rest_framework import serializers

from . import models


class PlayerSerializer(serializers.ModelSerializer):
    # games = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    # )

    class Meta:
        fields = "__all__"
        model = models.Player


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = models.Game
