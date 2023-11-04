import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv("sales_data_2.csv")

# Convert the 'Date' column to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the daily gross profit
df['Daily Gross Profit'] = df['Selling price'] - df['Buying price']

# Calculate the 3-day rolling average of daily gross profit
df['3-Day Avg Gross Profit'] = df['Daily Gross Profit'].rolling(window=3).mean()

# 3. Optimize the sales process to ensure gross margin is maximized:
# a. Calculate profit for each vendor
vendor_profit = df.groupby("Firm bought from")["Selling price"].sum() - df.groupby("Firm bought from")["Buying price"].sum()
# b. Calculate profit for each customer
customer_profit = df.groupby("Customer")["Selling price"].sum() - df.groupby("Customer")["Buying price"].sum()

# 4. Calculate the 25th, 50th (median), and 75th percentiles for both buying and selling prices:
percentiles = df[['Buying price', 'Selling price']].quantile([0.25, 0.5, 0.75])

# 5. Analyze how often prices fall below the 25th percentile or above the 75th percentile:
below_25th = df[df['Selling price'] < percentiles.loc[0.25]['Selling price']]
above_75th = df[df['Selling price'] > percentiles.loc[0.75]['Selling price']]

# Print the results
print("1. 3-Day Average Gross Profit:")
print(df[['Date', '3-Day Avg Gross Profit']])
print("\n2. Insights into 3-Day Trend Changes:")
# You can plot the 3-day average trend over time here.
print("\n3. Vendor Profit:")
print(vendor_profit)
print("\nCustomer Profit:")
print(customer_profit)
print("\n4. Percentiles for Buying and Selling Prices:")
print("25th Percentile:")
print(percentiles.loc[0.25])
print("\nMedian (50th Percentile):")
print(percentiles.loc[0.5])
print("\n75th Percentile:")
print(percentiles.loc[0.75])
print("\n5. Frequency of Prices Below 25th Percentile:")
print(len(below_25th))
print("\nFrequency of Prices Above 75th Percentile:")
print(len(above_75th))
