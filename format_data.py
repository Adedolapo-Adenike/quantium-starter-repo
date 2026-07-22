import pandas as pd

# Load all three CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine all three into one DataFrame
all_data = pd.concat([df0, df1, df2])

# Keep only Pink Morsel rows
pink_morsels = all_data[all_data['product'] == 'pink morsel']

# Clean the price column: remove '$' and convert to a number
pink_morsels['price'] = pink_morsels['price'].str.replace('$', '', regex=False).astype(float)

# Calculate sales = price * quantity
pink_morsels['sales'] = pink_morsels['price'] * pink_morsels['quantity']

# Keep only the three fields we need
output = pink_morsels[['sales', 'date', 'region']]

# Save to a new CSV file
output.to_csv('formatted_sales_data.csv', index=False)

print("Formatted data saved successfully.")