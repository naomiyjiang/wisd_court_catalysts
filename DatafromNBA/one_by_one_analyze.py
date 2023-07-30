import pandas as pd

# 读取数据
df = pd.read_csv('player_analyze_result.csv')

# 获取所需的队伍列表
teams = ['Boston Celtics', 'Miami Heat', 'Dallas Mavericks', 'Golden State Warriors']

# 新建一个空的DataFrame来保存统计数据
new_df = pd.DataFrame()

# 对每个队伍进行数据处理
for team in teams:
    # 筛选出当前队伍的数据
    team_data = df[df['team_name'] == team]
    
    # 通过player_id对数据进行分组，并计算累加和以及投篮次数
    group_data = team_data.groupby('player_id').agg(
        player_name=pd.NamedAgg(column='player_name', aggfunc='first'),
        team_name=pd.NamedAgg(column='team_name', aggfunc='first'),
        _1pt_made=pd.NamedAgg(column='1pt_made', aggfunc='sum'),
        _2pt_made=pd.NamedAgg(column='2pt_made', aggfunc='sum'),
        _3pt_made=pd.NamedAgg(column='3pt_made', aggfunc='sum'),
        _1pt_missed=pd.NamedAgg(column='1pt_missed', aggfunc='sum'),
        _2pt_missed=pd.NamedAgg(column='2pt_missed', aggfunc='sum'),
        _3pt_missed=pd.NamedAgg(column='3pt_missed', aggfunc='sum'),
        games_played=pd.NamedAgg(column='game_id', aggfunc='nunique'),
    )
    
    # 计算总的投篮次数
    group_data['_1pt_total'] = group_data['_1pt_made'] + group_data['_1pt_missed']
    group_data['_2pt_total'] = group_data['_2pt_made'] + group_data['_2pt_missed']
    group_data['_3pt_total'] = group_data['_3pt_made'] + group_data['_3pt_missed']

    # 计算命中率，并将其格式化为百分数
    group_data['_1pt_shooting_percentage'] = (group_data['_1pt_made'] / group_data['_1pt_total']).map("{:.2%}".format)
    group_data['_2pt_shooting_percentage'] = (group_data['_2pt_made'] / group_data['_2pt_total']).map("{:.2%}".format)
    group_data['_3pt_shooting_percentage'] = (group_data['_3pt_made'] / group_data['_3pt_total']).map("{:.2%}".format)

    # 将当前队伍的统计数据添加到新的DataFrame中
    new_df = new_df.append(group_data.reset_index())

# 保存新的统计数据到CSV文件中
new_df.to_csv('player_onebyone_analyze.csv', index=False)


