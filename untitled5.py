# number of different songs listened in a month

import json
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON data
with open('/Users/kadirzabun/Desktop/Courses/DSA 210/Project/Python Files/Spotify Extended Streaming History/Streaming_History_Audio_2018-2022_0.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

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
plt.figure(figsize=(12, 6))
plt.plot(song_variety['month_year'], song_variety['distinct_songs_count'], marker='o')
plt.title('Number of Distinct Songs Listened Per Month')
plt.xlabel('Month-Year')
plt.ylabel('Number of Distinct Songs')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()