# listening time of the most listened 10 songs over months 


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

# Group by track and calculate total listening time
track_listening = df.groupby('master_metadata_track_name')['ms_played'].sum().reset_index()

# Get top 10 songs by total listening time
top_10_songs = track_listening.nlargest(10, 'ms_played')['master_metadata_track_name'].tolist()

# Filter data for the top 10 songs
df_top_10 = df[df['master_metadata_track_name'].isin(top_10_songs)]

# Group by song and month-year, summing listening time
monthly_listening = df_top_10.groupby(['master_metadata_track_name', 'month_year'])['ms_played'].sum().reset_index()

# Convert ms_played to hours for better readability
monthly_listening['listening_hours'] = monthly_listening['ms_played'] / (1000 * 60 * 60)

# Plot each song's listening trend
for song in top_10_songs:
    song_data = monthly_listening[monthly_listening['master_metadata_track_name'] == song]
    plt.figure(figsize=(10, 6))
    plt.plot(song_data['month_year'].astype(str), song_data['listening_hours'], marker='o')
    plt.title(f'Monthly Listening Time for "{song}"')
    plt.xlabel('Month-Year')
    plt.ylabel('Listening Time (Hours)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()