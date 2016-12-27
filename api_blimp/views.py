from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest_framework import generics, mixins, permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers
import datetime


def clean_unity_data(incoming_dict):
    cleaned_data = {}
    for key, value in incoming_dict.items():
        # print("Key: {}  value:  {}".format(key, value))
        if "-" in value[0]:
            non_negative = value.replace("-", "")
            cleaned_data[key] = -float(non_negative)
        else:
            cleaned_data[key] = value
    return cleaned_data


class ListCreatePlayer(generics.ListCreateAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class CreateListGame(generics.ListCreateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

@csrf_exempt
@require_http_methods(["POST"])
def UpdateGame(request, game_pk):
    # need to update a queryset, not just a single record

    location_points = request.POST.copy()
    update_dict = clean_unity_data(location_points)

    game_update = models.Game.objects.filter(pk=game_pk).update(**update_dict)
    game = models.Game.objects.get(pk=game_pk)
    game_serializer = serializers.GameSerializer(game)

    status_code = status.HTTP_200_OK
    return JsonResponse(game_serializer.data, status=status_code)


@csrf_exempt
@require_http_methods(["POST"])
def CreateProjectile(request, game_pk):
    game = models.Game.objects.get(pk=game_pk)
    projectile_info = request.POST.copy()
    cleaned_data = clean_unity_data(projectile_info)
    projectile = models.Projectile.objects.create(game=game, **cleaned_data)

    serializer = serializers.ProjectileSerializer(projectile)

    return JsonResponse(serializer.data, status=status.HTTP_200_OK)



class GetGame(generics.RetrieveAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    lookup_url_kwarg = "game_pk"


@require_http_methods(["GET"])
def ListUnusedProjectiles(request, game_pk):
    unused_projectiles = models.Projectile.objects.filter(game__pk=game_pk, rendered_in_enemy_client=False)
    unused_projectiles.update(rendered_in_enemy_client=True)
    serializer = serializers.ProjectileSerializer(unused_projectiles)
    return JsonResponse(serializer.data, status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def GameSearcher(request):
    if request.method.lower() == "post":
        # Serialize "new" member's email
        serializer = serializers.SearchingPlayerSerializer(data=request.POST)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        print("Player ID sent in: {}".format(serializer.validated_data["player_id"]))
        try:
            searching_player = models.Player.objects.get(pk=serializer.validated_data["player_id"])
        except models.Player.DoesNotExist:
            return JsonResponse({"message": "Player doesn't exist!"},
                            status=status.HTTP_403_FORBIDDEN)

        available_game = models.Game.objects.filter(Q(good_guy__isnull=True) |
                                                    Q(bad_guy__isnull=True)).first()
        if not available_game:
            # create game
            available_game = models.Game.objects.create(good_guy=searching_player)
            status_code = status.HTTP_201_CREATED
        elif not available_game.good_guy:
            # spawn player as good guy
            available_game.good_guy = searching_player
            available_game.save()
            status_code = status.HTTP_200_OK
        elif not available_game.bad_guy:
            # spawn player as bad guy
            available_game.bad_guy = searching_player
            available_game.save()
            status_code = status.HTTP_200_OK
        print(available_game)
        serialized_game = serializers.GameSerializer(available_game)

        return JsonResponse(serialized_game.data,
                            status=status_code)
    else:
        return JsonResponse({"message": "Only posts allowed here"},
                            status=status.HTTP_403_FORBIDDEN)
