import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from nbadle.models import Team, Player
print('import_data.py is running')




def import_teams_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            team_code = row[0]
            name = row[1]  # Replace 'name' with the actual column name in your CSV file
            conference = row[2]  # Replace 'Conference' with the actual column name in your CSV file

            team = Team(team_code=team_code, name=name, conference=conference)
            team.save()
            print(f"Team '{name}' added successfully.")

# Provide the file path of the CSV file
teams_file_path = r'C:\Users\jerem\OneDrive\Desktop\NBA-Team-Names.csv'
import_teams_from_csv(teams_file_path)


def import_players():
    player_data = [
        {
            'name': 'Joel Embiid',
            'position': 'C-F',
            'college': 'Kansas',
            'team_name': 'Philadelphia 76ers',
            'img_url': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3059318.png&h=80&w=110&scale=crop',
            'ppg': 23.7,
            'apg': 9.8,
            'rpg': 2.7,
            'spg': 0.7,
            'bpg': 2.8,
            'offensive_rating': 105,
            'defensive_rating': 106.6,
            'height': "7' 0\"",
            'weight': '280 lbs'
        }
    ]

    for data in player_data:
        name = data['name']
        position = data['position']
        college = data['college']
        team_name = data['team_name']
        img_url = data['img_url']
        ppg = data['ppg']
        apg = data['apg']
        rpg = data['rpg']
        spg = data['spg']
        bpg = data['bpg']
        offensive_rating = data['offensive_rating']
        defensive_rating = data['defensive_rating']
        height = data['height']
        weight = data['weight']

        try:
            team = Team.objects.get(name=team_name)
        except Team.DoesNotExist:
            print(f"Team '{team_name}' does not exist. Skipping player '{name}'.")
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
            offensive_rating=offensive_rating,
            defensive_rating=defensive_rating,
            height=height,
            weight=weight,
        )
        print(player)
        player.save()

    print('Players imported successfully.')




# import_teams()
# import_players()


# def import_teams():
#     print('starting to put teams')
    # teams_file_path = r'C:\Users\jerem\OneDrive\Desktop\NBA-Team-Names.csv'

    # encodings = ['utf-8', 'latin-1', 'cp1252']

    # for encoding in encodings:
    #     try:
    #         with open(teams_file_path, 'r', encoding=encoding) as csvfile:
    #             reader = csv.DictReader(csvfile)
    #             for row in reader:
    #                 name = row['name']
    #                 conference = row['Conference']
    #                 team_code = row['Team Code']

    #                 team = Team(name=name, conference=conference, team_code=team_code)
    #                 print(team)
    #                 team.save()

    #         print('Teams imported successfully.')
    #         return  # Exit the function if import is successful
    #     except Exception as e:
    #         print(f'Error importing teams: {e}')

    # print('Failed to import teams.')





# def import_players():
#     players_file_path = r'C:\Users\jerem\OneDrive\Desktop\Book1.csv'

#     encodings = ['utf-8', 'latin-1', 'cp1252']

#     for encoding in encodings:
#         try:
#             with open(players_file_path, 'r', encoding=encoding) as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     name = row['NAME']
#                     position = row['POS']
#                     college = row['college']
#                     team_name = row['TEAM']
#                     img_url = row['player_img']
#                     ppg = row['PPG']
#                     apg = row['APG']
#                     rpg = row['RPG']
#                     spg = row['SPG']
#                     bpg = row['BPG']
#                     offensive_rating = row['ORtg']
#                     defensive_rating = row['DRtg']
#                     height = row['height']
#                     weight = row['weight']

#                     try:
#                         team = Team.objects.get(name=team_name)
#                     except Team.DoesNotExist:
#                         print(f"Team '{team_name}' does not exist. Skipping player '{name}'.")
#                         continue

#                     player = Player(
#                         name=name,
#                         position=position,
#                         college=college,
#                         team=team,
#                         img_url=img_url,
#                         ppg=ppg,
#                         apg=apg,
#                         rpg=rpg,
#                         spg=spg,
#                         bpg=bpg,
#                         offensive_rating=offensive_rating,
#                         defensive_rating=defensive_rating,
#                         height=height,
#                         weight=weight,
#                     )
#                     print(player)
#                     player.save()

#             print('Players imported successfully.')
#             return  # Exit the function if import is successful
#         except Exception as e:
#             print(f'Error importing players: {e}')

#     print('Failed to import players.')


