import csv
import os

def calculate_player_stats(csv_file, player_id):
    points_data = {
        1: {'made': 0, 'missed': 0},
        2: {'made': 0, 'missed': 0},
        3: {'made': 0, 'missed': 0}
    }

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_type = int(row['event_type'])
            opt1 = int(row['opt1'])
            current_player_id = int(row['player1_id'])
            current_team_id = int(row['team_id'])

            if current_player_id == player_id and event_type in [1, 2, 3]:
                if event_type == 1:
                    if opt1 == 3:
                        points_data[3]['made'] += 1
                    elif opt1 == 2:
                        points_data[2]['made'] += 1
                elif event_type == 2:
                    if opt1 == 3:
                        points_data[3]['missed'] += 1
                    elif opt1 == 2:
                        points_data[2]['missed'] += 1
                elif event_type == 3:
                    if opt1 == 1:
                        points_data[1]['made'] += 1
                    elif opt1 == 2:
                        points_data[1]['missed'] += 1

    results = {}
    for points, data in points_data.items():
        made_shots = data['made']
        missed_shots = data['missed']
        total_shots = made_shots + missed_shots
        if total_shots > 0:
            shooting_percentage = round((made_shots / total_shots) * 100, 2)
        else:
            shooting_percentage = 0

        results[f'{points}pt_shooting_percentage'] = shooting_percentage
        results[f'{points}pt_made'] = made_shots
        results[f'{points}pt_missed'] = missed_shots
        results[f'{points}pt_total'] = total_shots

    return results


def write_player_stats_to_csv(csv_files, output_file):
    header = ['game_id', 'player_id', '1pt_shooting_percentage', '2pt_shooting_percentage', '3pt_shooting_percentage',
              '1pt_made', '2pt_made', '3pt_made', '1pt_missed', '2pt_missed', '3pt_missed', '1pt_total', '2pt_total', '3pt_total']

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for csv_file in csv_files:
            game_id = os.path.basename(csv_file).split('.')[0]
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                player_ids = set()
                for row in reader:
                    player_id = int(row['player1_id'])
                    player_ids.add(player_id)

                for player_id in player_ids:
                    player_stats = calculate_player_stats(csv_file, player_id)
                    if any(player_stats.values()):
                        row = [game_id, player_id]
                        for key in header[2:]:
                            row.append(player_stats[key])
                        writer.writerow(row)



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
output_file = 'player_analyze_result_row_data.csv'

write_player_stats_to_csv(csv_files, output_file)
