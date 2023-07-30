import csv
import os

def get_team_and_player_ids(csv_file):
    ids = set()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_id = int(row['player1_id'])
            team_id = int(row['team_id'])
            if player_id != 0 and team_id != 0:  # Ignore rows where player_id or team_id is 0
                ids.add((player_id, team_id))
    return ids

def write_team_and_player_ids_to_csv(csv_files, output_file):
    header = ['player_id', 'team_id']

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for csv_file in csv_files:
            ids = get_team_and_player_ids(csv_file)
            for player_id, team_id in ids:
                writer.writerow([player_id, team_id])

# Example usage
csv_files = [
    'data/g0042100301.csv',
    'data/g0042100302.csv',
    'data/g0042100303.csv',
    'data/g0042100304.csv',
    'data/g0042100305.csv',
    'data/g0042100306.csv',
    'data/g0042100307.csv',
    'data/g0042100311.csv',
    'data/g0042100312.csv',
    'data/g0042100313.csv',
    'data/g0042100314.csv',
    'data/g0042100315.csv',
    'data/g0042100401.csv',
    'data/g0042100402.csv',
    'data/g0042100403.csv',
    'data/g0042100404.csv',
    'data/g0042100405.csv'
]
output_file = 'team_and_player_ids.csv'

write_team_and_player_ids_to_csv(csv_files, output_file)


