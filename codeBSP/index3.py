import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'BSP_Dong.csv'  # Replace with the correct file path
data = pd.read_csv(file_path)

# Convert the SaleDate column to datetime format
data['SaleDate'] = pd.to_datetime(data['SaleDate'], errors='coerce')

# Drop any rows where SaleDate is NaT (not a time)
data = data.dropna(subset=['SaleDate'])

# Line chart: Change in total sales amount over time
daily_sales = data.groupby('SaleDate')['TotalAmount'].sum()

# Plotting the sales over time
plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
