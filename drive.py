import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Book1.csv")

# 1. Calculate the overall gross margin
overall_gross_margin = (df["Selling price"] - df["Buying price"]).sum()

# 2. Calculate the profit for each vendor (Firm bought from)
vendor_profit = df.groupby("Firm bought from")["Selling price"].sum() - df.groupby("Firm bought from")["Buying price"].sum()
most_profitable_vendor = vendor_profit.idxmax()

# 3. Calculate the profit for each customer
customer_profit = df.groupby("Customer")["Selling price"].sum() - df.groupby("Customer")["Buying price"].sum()
least_profitable_customer = customer_profit.idxmin()

# 4. Calculate the most profitable day of the week
df["Date"] = pd.to_datetime(df["Date"])
df["Day of Week"] = df["Date"].dt.day_name()
day_profit = df.groupby("Day of Week")["Selling price"].sum() - df.groupby("Day of Week")["Buying price"].sum()
most_profitable_day = day_profit.idxmax()

# 5. Calculate the least profitable day of the week
least_profitable_day = day_profit.idxmin()

# Print the results
print("1. Overall Gross Margin:", overall_gross_margin)
print("2. Most Profitable Vendor:", most_profitable_vendor)
print("3. Least Profitable Customer:", least_profitable_customer)
print("4. Most Profitable Day of the Week:", most_profitable_day)
print("5. Least Profitable Day of the Week:", least_profitable_day)
