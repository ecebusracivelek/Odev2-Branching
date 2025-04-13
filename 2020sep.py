import pandas as pd
import matplotlib.pyplot as plt

# Assuming your dataframe is named 'df'
# Replace 'your_data.csv' with the actual file or data source

# Read the data
df = pd.read_csv('https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/ef34bd55-86d8-4459-a710-79de30a45be2/download/traffic_density_202009.csv')

# Filter rows where GEOHASH is 'sxk9sf'
filtered_df = df[df['GEOHASH'] == 'sxk9sf']

# Find max and min speeds and corresponding dates
max_speed_row = filtered_df.loc[filtered_df['MAXIMUM_SPEED'].idxmax()]
min_speed_row = filtered_df.loc[filtered_df['MINIMUM_SPEED'].idxmin()]
max_avg_speed_row = filtered_df.loc[filtered_df['AVERAGE_SPEED'].idxmax()]
min_avg_speed_row = filtered_df.loc[filtered_df['AVERAGE_SPEED'].idxmin()]

# Print results
print("Maximum Speed:")
print(f"Date: {max_speed_row['DATE_TIME']}, Speed: {max_speed_row['MAXIMUM_SPEED']}")
print(f"Number of Vehicles: {max_speed_row['NUMBER_OF_VEHICLES']}")
print(f"Average Speed: {max_speed_row['AVERAGE_SPEED']}")

print("Minimum Speed:")
print(f"Date: {min_speed_row['DATE_TIME']}, Speed: {min_speed_row['MINIMUM_SPEED']}")
print(f"Number of Vehicles: {min_speed_row['NUMBER_OF_VEHICLES']}")
print(f"Average Speed: {min_speed_row['AVERAGE_SPEED']}")

print("Maximum Average Speed:")
print(f"Date: {max_avg_speed_row['DATE_TIME']}, Speed: {max_avg_speed_row['AVERAGE_SPEED']}")
print(f"Number of Vehicles: {max_avg_speed_row['NUMBER_OF_VEHICLES']}")
print(f"Maximum Speed: {max_avg_speed_row['MAXIMUM_SPEED']}")
print(f"Minimum Speed: {max_avg_speed_row['MINIMUM_SPEED']}")
print("Minimum Average Speed:")
print(f"Date: {min_avg_speed_row['DATE_TIME']}, Speed: {min_avg_speed_row['AVERAGE_SPEED']}")
print(f"Number of Vehicles: {min_avg_speed_row['NUMBER_OF_VEHICLES']}")
print(f"Maximum Speed: {min_avg_speed_row['MAXIMUM_SPEED']}")
print(f"Minimum Speed: {min_avg_speed_row['MINIMUM_SPEED']}")

# Assuming your 'DATE_TIME' column is in datetime format
df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])

# Extract date and hour information
df['Date'] = df['DATE_TIME'].dt.date
df['Hour'] = df['DATE_TIME'].dt.hour

# Calculate daily average traffic volume
daily_avg_traffic = df.groupby(['Date', 'Hour'])['NUMBER_OF_VEHICLES'].mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
for date, group in daily_avg_traffic.groupby('Date'):
    plt.plot(group['Hour'], group['NUMBER_OF_VEHICLES'], label=str(date))

plt.title('Daily Average Traffic Volume')
plt.xlabel('Hour')
plt.ylabel('Average Traffic Volume')
plt.legend()
plt.show()
