__author__ = 'davidaxelrod'
from django.shortcuts import get_object_or_404, render
from django.db.models import Q, F
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest_framework import generics, mixins, permissions, viewsets, status
from rest_framework.response import Response

from api_blimp import models



def UnivInnoFellows(request):

    return render(request, "api_blimp/index.html")