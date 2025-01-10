Sabanci University DSA 210 Introduction to Data Science Course Fall 2024-2025 Term Project.

# Spotify and Activity Data Analysis

## Description ##
This project analyzes the relationship between my step count and the amount of time I spent listening music. First I looked at the distribution of my daily step count and the distribution of the amount of time I spent listening to music. I looked at the monthly and the daily distributions so that I can analyze the data more accurately. I had almost a 7 year data from my streaming history but there was not quite available data for my step count. So while visualizing the data seperately, I used all the data for each graph. When I combined them to see the whether there is a relationship between them, I used only the time periods when each data are available and there is no missing slots. 


## Motivation ##
Music is something I often enjoy while walking or commuting. I noticed that I tend to listen to music regularly during these times, and this made me curious about whether my music listening habits might have any connection to my physical activity, specifically my step count.
This project aims to explore patterns in my data by analyzing my Spotify listening history alongside my daily step count from the Apple Health app. By combining these two datasets, I hope to identify if there is any observable relationship between the music I listen to and how active I am throughout the day.

## Data Source ##
### Spotify Data ###

I used the Spotify API to extract detailed listening history, including:
	•	Track Details: Information about the songs, such as their title, artist, and album.
	•	Listening Timestamps: The precise times when I listened to each track.
	•	Listening Durations: The amount of time I spent listening to specific tracks or playlists.

This data allowed me to analyze my listening habits, such as the frequency of repeated songs and the times of day I listened to music, which I then compared to my physical activity data.

### Apple Health Data ###

I collected physical activity data from the iPhone Health App, focusing on the step count. I used this data because other data parameters such as walking distance, energy burned may have changed according to other parameters such as height and weight during this period, causing the data to be wrongly analzed.

This data provided a quantitative measure of my physical activity, which I analyzed alongside the Spotify listening data to identify potential patterns or correlations.

Data Integration

The timestamps from both datasets were aligned to find overlaps between music listening sessions and physical activity. This allowed for a more detailed analysis of whether certain music listening habits corresponded with variations in step count or other activity metrics.

Note

Google Maps data was initially considered but not used in this analysis, as the focus remained solely on the Spotify listening history and step count data from the Apple Health app.





