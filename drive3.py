import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the CSV file into a DataFrame
df = pd.read_csv("sales_data_2.csv")

# Calculate the gross margin without honoring Vendor 4
gross_margin_without_vendor_4 = (df[df['Firm bought from'] != 'Vendor 4']['Selling price'] - df[df['Firm bought from'] != 'Vendor 4']['Buying price']).sum()

# Calculate the gross margin with honoring Vendor 4
gross_margin_with_vendor_4 = (df['Selling price'] - df['Buying price']).sum()

# Calculate the impact on gross margin
impact_on_gross_margin = gross_margin_with_vendor_4 - gross_margin_without_vendor_4

# Calculate the gross margin for each vendor
vendor_gross_margin = (df.groupby("Firm bought from")["Selling price"].sum() - df.groupby("Firm bought from")["Buying price"].sum())

# Identify the vendor with the highest gross margin
best_vendor = vendor_gross_margin.idxmax()

# Calculate the theoretical maximum gross margin
theoretical_max_margin = vendor_gross_margin.max()

# Assuming you have price and sales data in 'Selling price' and 'Quantity sold' columns
price = df['Selling price']
sales = df['Quantity sold']

# Perform a linear regression to estimate price elasticity
X = sm.add_constant(price)
model = sm.OLS(sales, X).fit()

# Get the coefficient for price (price elasticity)
price_elasticity = model.params['Selling price']

# Print the results
print("1. Impact on Gross Margin by Honoring Vendor 4:", impact_on_gross_margin)
print("\n2. Vendor with Highest Gross Margin:", best_vendor)
print("Theoretical Maximum Gross Margin:", theoretical_max_margin)
print("\n3. Price Elasticity of Sapota:", price_elasticity)
