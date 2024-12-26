# listening time over months


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

# Group by month-year and sum listening time
monthly_listening = df.groupby('month_year')['ms_played'].sum().reset_index()
monthly_listening['month_year'] = monthly_listening['month_year'].astype(str)

# Convert ms_played to hours for better visualization
monthly_listening['listening_hours'] = monthly_listening['ms_played'] / (1000 * 60 * 60)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(monthly_listening['month_year'], monthly_listening['listening_hours'], marker='o')
plt.title('Listening Time Over Months')
plt.xlabel('Month-Year')
plt.ylabel('Listening Time (Hours)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()