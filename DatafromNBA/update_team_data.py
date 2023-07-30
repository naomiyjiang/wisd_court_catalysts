import csv
import json

# 步骤1：读取player_analyze_result_row_data.csv
data = []
with open('team_analyze_result_row_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
 
# 步骤3：读取teams.json
with open('data/teams.json', 'r') as jsonfile:
    teams_data = json.load(jsonfile)

# 步骤4：创建用于team_analyze_result.csv数据的新列表
result_data = []

#处理每一行并添加球队名称列
for row in data: 
    team_id = row['team_id']
 
    # 步骤7：查找球队名称
    team = next((t for t in teams_data['teams'] if t['nbaId'] == int(team_id)), None)
    if team:
        team_name = team['name']
        row['team_name'] = team_name

    # 步骤8：重新排列列的顺序
    new_row = {
        'game_id': row['game_id'],
        'team_id': team_id, 
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

# 步骤10：将result_data写入player_analyze_result.csv
fieldnames = list(result_data[0].keys())
with open('team_analyze_result.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result_data)
