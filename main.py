import pandas as pd
import os
from datetime import datetime

# Read the source excel file into a pandas DataFrame 
df = pd.read_excel('source_file.xlsx') 

# Convert date columns to datetime objects
df['Planned Cutover date'] = pd.to_datetime(df['Planned Cutover date'], format='%d-%m-%Y', errors='coerce')
df['Actual Cutover date'] = pd.to_datetime(df['Actual Cutover date'], format='%d-%m-%Y', errors='coerce')

# Filter the DataFrame based on the specified conditions
filtered_df = df[(df['Planned Cutover date'] > datetime.today()) & 
                 (df['Planned Cutover date'] < datetime(2025, 1, 1)) & 
                 (df['Actual Cutover date'].isnull()) & 
                 (df['Entity'] == 'AXA UK & Ireland')]
                 # (df['App State'] != '2.2/ Migration On Going')]

# Group the DataFrame by the 'Environment' column 
grouped = filtered_df.groupby('Environment') 
mydir = 'C:/Users/B449OH/Downloads/coding/servers_split_by_envs/results' 

# Iterate through the groups and create separate excel files for each environment 
for environment, group in grouped: 
    environment = environment.replace('/', ' - ').replace('?', ' - ').replace(':', ' - ').replace('\\', ' - ')
    output_file_name = environment + '.xlsx' 
    output_path = os.path.join(mydir,output_file_name) 
    group[['Environment','Source server']].to_excel(output_path, index=False)
