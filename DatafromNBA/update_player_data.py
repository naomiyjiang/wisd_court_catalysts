import csv
import json

 
data = []
with open('player_analyze_result_row_data_with_team.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

 
with open('data/players.json', 'r') as jsonfile:
    players_data = json.load(jsonfile)

 
with open('data/teams.json', 'r') as jsonfile:
    teams_data = json.load(jsonfile)

 
result_data = []

 
for row in data:
    player_id = row['player_id']
    team_id = row['team_id']

 
    player = next((p for p in players_data['players'] if p['nbaId'] == int(player_id)), None)
    if player:
        player_name = player['firstName'] + ' ' + player['lastName']
        row['player_name'] = player_name

 
    team = next((t for t in teams_data['teams'] if t['nbaId'] == int(team_id)), None)
    if team:
        team_name = team['name']
        row['team_name'] = team_name

      
    new_row = {
        'game_id': row['game_id'],
        'team_id': team_id,
        'player_id': player_id,
        'player_name': player_name,
        'team_name': team_name,
        '1pt_shooting_percentage': row['1pt_shooting_percentage'],
        '2pt_shooting_percentage': row['2pt_shooting_percentage'],
        '3pt_shooting_percentage': row['3pt_shooting_percentage'],
        '1pt_made': row['1pt_made'],
        '2pt_made': row['2pt_made'],
        '3pt_made': row['3pt_made'],
        '1pt_missed': row['1pt_missed'],
        '2pt_missed': row['2pt_missed'],
        '3pt_missed': row['3pt_missed'],
        '1pt_total': row['1pt_total'],
        '2pt_total': row['2pt_total'],
        '3pt_total': row['3pt_total']
    }

    result_data.append(new_row)

 
fieldnames = list(result_data[0].keys())
with open('player_analyze_result.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result_data)
