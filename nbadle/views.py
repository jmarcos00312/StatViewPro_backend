from django.shortcuts import render
from django.http import JsonResponse
from nbadle.models import Player
# Create your views here.

def get_all_Players(request):
    players = Player.objects.all()
    data = {
        'players' : list(players.values())
    }
    return JsonResponse(data)