import csv

# Step 1: Read the contents of the two CSV files
player_analyze_result_file = "player_analyze_result_row_data.csv"
team_and_player_ids_file = "team_and_player_ids_cleaned.csv"

player_data = {}
with open(team_and_player_ids_file, "r", newline="") as file:
    team_and_player_ids_reader = csv.reader(file)
    next(team_and_player_ids_reader)  # Skip the header row
    for row in team_and_player_ids_reader:
        player_id, team_id = int(row[0]), int(row[1])
        player_data[player_id] = team_id

# Step 3: Add the team_id to the player_analyze_result_data
output_file = "player_analyze_result_row_data_with_team.csv"
with open(player_analyze_result_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    header.insert(1, "team_id")  # Add "team_id" as the second column
    writer.writerow(header)

    for row in reader:
        player_id = int(row[1])
        team_id = player_data.get(player_id, "N/A")
        row.insert(1, team_id)  # Add "team_id" value at the second position
        writer.writerow(row)

print(f"Updated data written to {output_file}")

