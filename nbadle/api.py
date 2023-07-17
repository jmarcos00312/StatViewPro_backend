from rest_framework.decorators import api_view
from rest_framework.response import Response
from nbadle.models import Player
from django.http import JsonResponse
# import 

@api_view(['GET'])
def get_76ers_players(request):
    players = Player.objects.filter(team__name='Philadelphia 76ers')
    data = []
    for player in players:
        data.append({
            'name': player.name,
            'position': player.position,
            'college': player.college,
            'team': player.team.name,
            'img_url': player.img_url,
            'ppg': player.ppg,
            'apg': player.apg,
            'rpg': player.rpg,
            'spg': player.spg,
            'bpg': player.bpg,
            'fg_percent': player.fg_percent,
            'three_pt_percent': player.three_pt_percent,
            'ft_percent': player.ft_percent,
            'fpg': player.fpg,
            'height': player.height,
            'weight': player.weight,
        })
    return Response(data)

def get_all_players(request):
    players = Player.objects.all()
    data = {
        'players': list(players.values())
    }
    return JsonResponse(data)

def start_level_one(request):
    pass