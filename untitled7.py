# the average listening time per song per month

import json
import pandas as pd
import matplotlib.pyplot as plt
import glob

# Define the folder path where the JSON files are stored
folder_path = '/Users/kadirzabun/Desktop/Courses/DSA 210/Project/Python Files/Spotify Extended Streaming History/'  # Replace with the actual path

# Get all JSON files in the folder
file_list = glob.glob(folder_path + '*.json')

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through each file and read the data
for file in file_list:
    with open(file, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        data_frames.append(df)

# Concatenate all DataFrames into one
df = pd.concat(data_frames, ignore_index=True)

# Ensure `ts` is datetime and extract month-year
df['ts'] = pd.to_datetime(df['ts'])
df['month_year'] = df['ts'].dt.to_period('M')

# Calculate total listening time per month
monthly_listening_time = df.groupby('month_year')['ms_played'].sum().reset_index()
monthly_listening_time.rename(columns={'ms_played': 'total_listening_time'}, inplace=True)

# Drop duplicate songs within each month
distinct_songs = df[['month_year', 'master_metadata_track_name']].drop_duplicates()

# Count the number of distinct songs per month
distinct_song_counts = distinct_songs.groupby('month_year')['master_metadata_track_name'].nunique().reset_index()
distinct_song_counts.rename(columns={'master_metadata_track_name': 'distinct_songs_count'}, inplace=True)

# Merge total listening time and distinct song counts
merged_data = pd.merge(monthly_listening_time, distinct_song_counts, on='month_year')

# Calculate average listening time per song
merged_data['average_listening_time_per_song'] = merged_data['total_listening_time'] / merged_data['distinct_songs_count']

# Convert ms to hours for better readability
merged_data['average_listening_time_per_song_hours'] = merged_data['average_listening_time_per_song'] / (1000 * 60 * 60)

# Convert month-year to string for plotting
merged_data['month_year'] = merged_data['month_year'].astype(str)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(merged_data['month_year'], merged_data['average_listening_time_per_song_hours'], marker='o')
plt.title('Average Listening Time Per Song Per Month')
plt.xlabel('Month-Year')
plt.ylabel('Average Listening Time Per Song (Hours)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()