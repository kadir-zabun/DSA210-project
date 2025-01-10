# number of different songs listened monthly

import json
import pandas as pd
import matplotlib.pyplot as plt

# Path to the Spotify JSON file
spotify_data_path = "/Users/kadirzabun/Desktop/Courses/DSA 210/Project/Python Files/Spotify Extended Streaming History/spotify_history_all.json"

# Load Spotify JSON data
with open(spotify_data_path, 'r') as f:
    spotify_data = json.load(f)

# Step 2: Create a DataFrame
spotify_df = pd.DataFrame(spotify_data)

# Step 3: Convert 'ts' (timestamp) to datetime
spotify_df['endTime'] = pd.to_datetime(spotify_df['ts'])

#  Ensure 'ms_played' is numeric
spotify_df['ms_played'] = pd.to_numeric(spotify_df['ms_played'], errors='coerce')

# Convert to DataFrame
df = pd.DataFrame(spotify_data)

# Ensure `ts` is datetime and extract month-year
df['ts'] = pd.to_datetime(df['ts'])
df['month_year'] = df['ts'].dt.to_period('M')
# Drop duplicate songs within each month
distinct_songs = df[['month_year', 'master_metadata_track_name']].drop_duplicates()

# Count the number of distinct songs per month
song_variety = distinct_songs.groupby('month_year')['master_metadata_track_name'].nunique().reset_index()
song_variety.rename(columns={'master_metadata_track_name': 'distinct_songs_count'}, inplace=True)

# Convert month-year to string for plotting
song_variety['month_year'] = song_variety['month_year'].astype(str)

# Plot the data
# Plot the histogram
plt.figure(figsize=(12, 6))
plt.bar(song_variety['month_year'], song_variety['distinct_songs_count'], color='skyblue', edgecolor='black')
plt.title('Number of Distinct Songs Listened Per Month', fontsize=16)
plt.xlabel('Month-Year', fontsize=12)
plt.ylabel('Number of Distinct Songs', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
