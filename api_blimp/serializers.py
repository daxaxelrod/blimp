__author__ = 'davidaxelrod'
from rest_framework import serializers

from . import models


class PlayerSerializer(serializers.ModelSerializer):
    # games = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    # )
    def create(self, validated_data):
        player, created = models.Player.objects.get_or_create(**validated_data)
        return player

    class Meta:
        fields = "__all__"
        model = models.Player


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = models.Game

class SearchingPlayerSerializer(serializers.Serializer):

    player_id = serializers.IntegerField()