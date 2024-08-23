import pandas as pd
from datetime import datetime

# Step 1: Read data from the BSP_Dong.csv file
file_path = 'BSP_Dong.csv'
df = pd.read_csv(file_path)

# Step 2: Check for missing data
missing_data = df.isnull().sum()
print("Missing data before handling:\n", missing_data)

# Step 3: Handle missing data
# Fill missing data in the 'SaleDate' column with the current date
df['SaleDate'].fillna(datetime.now().strftime('%Y-%m-%d'), inplace=True)

# Fill missing data in the 'Quantity' column with the mean value of the column
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

# Step 4: Check for and remove invalid data (negative values in the 'Quantity' column)
df = df[df['Quantity'] >= 0]

# Step 5: Save the cleaned data to a new file
output_path = 'BSP_Dong_cleaned.csv'
df.to_csv(output_path, index=False)

# Check again for missing data after handling
missing_data_after = df.isnull().sum()
print("Missing data after handling:\n", missing_data_after)

print("Data processing complete. The cleaned data has been saved to a new file: BSP_Dong_cleaned.csv")
