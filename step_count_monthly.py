#Monthly Step Count

import pandas as pd
import json
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Path to your Apple Health CSV file
health_data_path = "/Users/kadirzabun/Desktop/Courses/DSA 210/Project/Python Files/apple_health_data.csv"

#  Load the CSV file
health_df = pd.read_csv(health_data_path, low_memory=False)

#  Handle mixed data types
# Convert the 'value' column to numeric, forcing errors to NaN
health_df['value'] = pd.to_numeric(health_df['value'], errors='coerce')

#  Filter for step count data
# Filter rows where 'type' is 'HKQuantityTypeIdentifierStepCount'
step_count_df = health_df[health_df['type'] == 'HKQuantityTypeIdentifierStepCount']

#  Drop rows with missing or invalid values
step_count_df = step_count_df.dropna(subset=['value'])

# Assuming `step_count_df` has already been created
#  Convert startDate to datetime (if not already done)
step_count_df['startDate'] = pd.to_datetime(step_count_df['startDate'])

#  Ensure 'value' column is numeric
step_count_df['value'] = pd.to_numeric(step_count_df['value'], errors='coerce')

# Step 3: Extract the month-year from 'startDate'
step_count_df['month'] = step_count_df['startDate'].dt.to_period('M')  # Extract month-year

# Step 4: Aggregate total steps per month
monthly_steps = step_count_df.groupby('month')['value'].sum()

# Step 5: Exclude incomplete months (e.g., 2023-01 and 2025-01)
monthly_steps_filtered = monthly_steps.drop(['2023-01', '2025-01'], errors='ignore')

# Step 6: Plot the monthly walking steps
plt.figure(figsize=(12, 6))
monthly_steps_filtered.plot(kind='bar', color='lightgreen', edgecolor='black')

# Add titles and labels
plt.title("Monthly Walking Steps", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Steps", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
