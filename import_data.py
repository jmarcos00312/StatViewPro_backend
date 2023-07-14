import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from nbadle.models import Team, Player

print('import_data.py is running')

def import_teams_from_excel(file_path):
    print('Deleting teams before adding')
    Team.objects.all().delete()
    print('Teams deleted')
    df = pd.read_excel(file_path)
    
    for index, row in df.iterrows():
        team_code = row['Team Code']
        name = row['name']
        conference = row['Conference']
        
        team = Team(team_code=team_code, name=name, conference=conference)
        team.save()
        print(f"Team '{name}' added successfully.")

excel_file_path = 'C:\\Users\\jerem\\OneDrive\\Desktop\\NBA-Team-Names.xlsx'
import_teams_from_excel(excel_file_path)

print("=============================Starting to add players =============================")

def import_players_from_excel(file_path):
    print('Deleting Players before adding')
    Player.objects.all().delete()
    print('Players Deleted')
    
    df = pd.read_excel(file_path)
    
    for index, row in df.iterrows():
        name = row['NAME']
        position = row['POS']
        college = row['college']
        team_name = row['TEAM']
        img_url = row['player_img']
        ppg = row['PPG'] or 0
        apg = row['APG'] or 0
        rpg = row['RPG']or 0
        spg = row['SPG']or 0
        bpg = row['BPG']or 0
        mpg = row['MPG']or 0
        tpg = row['TPG']or 0
        offensive_rating = row['ORtg']or 0
        defensive_rating = row['DRtg']or 0
        height = row['height']
        weight = row['weight']
        
        try:
            team = Team.objects.get(name=team_name)
        except Team.DoesNotExist:
            print(f"Team '{team_name}' does not exist in the database. Skipping player '{name}'.")
            continue
        player = Player(
                name=name,
                        position=position,
                        college=college,
                        team=team,
                        img_url=img_url,
                        ppg=ppg,
                        apg=apg,
                        rpg=rpg,
                        spg=spg,
                        bpg=bpg,
                        mpg=mpg,
                        tpg=tpg,
                        offensive_rating=offensive_rating,
                        defensive_rating=defensive_rating,
                        height=height,
                        weight=weight,
                    )
        print(player)
        player.save()
        print(f"Player '{name}' added successfully.")

file_path = 'C:\\Users\\jerem\\OneDrive\\Desktop\\Book1.xlsx'
import_players_from_excel(file_path)        



#     print('Failed to import players.')


