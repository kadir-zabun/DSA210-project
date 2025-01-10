# number of different songs listened in a month

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



#  Ensure 'endTime' is in datetime format
spotify_df['endTime'] = pd.to_datetime(spotify_df['endTime'], errors='coerce')

#  Extract the month-year from 'endTime'
spotify_df['month'] = spotify_df['endTime'].dt.to_period('M')

#  Aggregate total listening time per month
monthly_listening_time = spotify_df.groupby('month')['ms_played'].sum()

#  Count the number of unique songs per month
monthly_unique_songs = spotify_df.groupby('month')['spotify_track_uri'].nunique()

#  Calculate average listening time per song
average_listening_time_per_song = monthly_listening_time / monthly_unique_songs

#  Convert milliseconds to minutes for better readability
average_listening_time_per_song_minutes = average_listening_time_per_song / (1000 * 60)

#  Display the result
print("Average Listening Time Per Song Per Month (minutes):")
print(average_listening_time_per_song_minutes)

#  Plot the results
plt.figure(figsize=(12, 6))
average_listening_time_per_song_minutes.plot(kind='bar', color='purple', edgecolor='black')

# Add labels, title, and formatting
plt.title("Average Listening Time Per Song Per Month", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Listening Time (Minutes)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
