import pandas as pd
import numpy as np

# Load your data (assuming 'data' is your DataFrame)
# Example: data = pd.read_csv('your_data_file.csv')
data = pd.read_pickle("../data/ko.pkl")

# Calculate the slopes
data['slope'] = data['4. close'].diff()

# Rolling window size (number of points to consider for slope)
window_size = 3  # You can adjust this value based on your needs

# Calculate rolling slopes using a rolling window
data['rolling_slope'] = data['slope'].rolling(window=window_size).mean()

# Check for constant slopes
data['is_constant_slope'] = data['rolling_slope'].diff().abs() < 1e-5  # Tolerance for slope change

# Create a mask to filter out constant slope segments
mask = data['is_constant_slope'].rolling(window=window_size).sum() < window_size

# Filter the data to exclude constant slope segments
filtered_data = data[~mask].copy()

# Drop temporary columns used for filtering
filtered_data.drop(columns=['slope', 'rolling_slope', 'is_constant_slope'], inplace=True)

# Plot the filtered data
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
sns.lineplot(data=filtered_data, x=filtered_data.index, y='4. close', label='Filtered Close Price')
plt.title('Filtered Close Prices Without Linear Segments')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
