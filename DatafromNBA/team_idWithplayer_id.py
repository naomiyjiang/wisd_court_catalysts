import pandas as pd

# 读取CSV文件
df = pd.read_csv('team_and_player_ids.csv')

# 去除重复的 (player_id, team_id) 组
df = df.drop_duplicates(subset=['player_id', 'team_id'])

# 检查每个 player_id 有多少个不同的 team_id
player_team_counts = df.groupby('player_id')['team_id'].nunique()

# 找出有多个 team_id 的 player_id
players_with_multiple_teams = player_team_counts[player_team_counts > 1].index

# 为这些 player_id 添加额外的值 1
for player in players_with_multiple_teams:
    df = df.append({'player_id': player, 'team_id': 1}, ignore_index=True)

# 将清洗后的数据写入新的CSV文件
df.to_csv('team_and_player_ids_clean_unfinished.csv', index=False)

