import sys
import os
import pandas as pd
from nbadle.models import Team, Player
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


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
        ppg = row['PPG']  if row['PPG'] is not None else -1
        apg = row['APG']  if row['APG'] is not None else -1
        rpg = row['RPG']  if row['RPG'] is not None else -1
        spg = row['SPG']  if row['SPG'] is not None else -1
        bpg = row['BPG']  if row['BPG'] is not None else -1
        mpg = row['MPG']  if row['MPG'] is not None else -1
        tpg = row['TPG']  if row['TPG'] is not None else -1
        fg_percent = row['fg_percent']  if row['fg_percent'] is not None else -1
        three_pt_percent = row['three_pt_percent'] if row['three_pt_percent'] is not None else -1
        ft_percent = row['ft_percent']  if row['ft_percent'] is not None else -1
        fpg = row['fpg']  if row['fpg'] is not None else -1
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
                        fg_percent=fg_percent,
                        three_pt_percent=three_pt_percent,
                        ft_percent=ft_percent,
                        fpg=fpg,
                        bpg=bpg,
                        mpg=mpg,
                        tpg=tpg,
                        height=height,
                        weight=weight,
                    )
        print(player)
        player.save()
        print(f"Player '{name}' added successfully to {team}")

file_path = 'C:\\Users\\jerem\\OneDrive\\Desktop\\merged_and_combined.xlsx'
import_players_from_excel(file_path) 



#     print('Failed to import players.')


