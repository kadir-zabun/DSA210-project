# listening time over months

import pandas as pd
import json
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
# Path to the Spotify JSON file
spotify_data_path = "/content/spotify_history_all.json"

# Load Spotify JSON data
with open(spotify_data_path, 'r') as f:
    spotify_data = json.load(f)

# Step 2: Create a DataFrame
spotify_df = pd.DataFrame(spotify_data)

# Step 3: Convert 'ts' (timestamp) to datetime
spotify_df['endTime'] = pd.to_datetime(spotify_df['ts'])

#  Ensure 'ms_played' is numeric
spotify_df['ms_played'] = pd.to_numeric(spotify_df['ms_played'], errors='coerce')
#  Extract the month from 'endTime'
spotify_df['month'] = spotify_df['endTime'].dt.to_period('M')  # Extract month-year

#  Aggregate total listening time per month
monthly_listening_time = spotify_df.groupby('month')['ms_played'].sum()

#  Convert milliseconds to hours
monthly_listening_time_hours = monthly_listening_time / (1000 * 60 * 60)

#  Plot the monthly listening times
plt.figure(figsize=(12, 6))
monthly_listening_time_hours.plot(kind='bar', color='skyblue', edgecolor='black')

# Add titles and labels
plt.title("Monthly Total Listening Time", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Listening Time (hours)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
