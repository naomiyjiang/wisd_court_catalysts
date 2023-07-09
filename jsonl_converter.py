# -*- coding: utf-8 -*-
"""
JSONL to CSV
"""

import json
import glob
import pandas as pd


jsonl_files = glob.glob('/Users/naomi/2023-hackathon/**/*.jsonl', recursive = True)
data_list = []


for file in jsonl_files:
    with open(file, 'r') as f:
        # Process each JSON file
        for line in f:
            print(line)  # Print the line
            data = json.loads(line)
            data_list.append(data)
            

# Convert the data list to a DataFrame
df = pd.DataFrame(data_list)
# Save the DataFrame to a CSV file
df.to_csv('/Users/naomi/2023-hackathon/output.csv', index=False)