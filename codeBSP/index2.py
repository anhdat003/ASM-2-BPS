import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the CSV file from the latest upload
file_path_latest = 'BSP_Dong.csv'
data = pd.read_csv(file_path_latest)

# Drop rows with missing target values
data_cleaned = data.dropna(subset=['TotalAmount'])

# Select features and target
features = ['Quantity', 'Discount']
X = data_cleaned[features]
y = data_cleaned['TotalAmount']

# Handle missing values in features
X.fillna(X.mean(), inplace=True)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the TotalAmount for the test set
y_pred = model.predict(X_test)

# Plotting the first 20 predicted values
plt.figure(figsize=(10, 6))
plt.plot(range(20), y_pred[:20], marker='o', label='Predicted TotalAmount')
plt.title('Predicted TotalAmount (First 20 values)')
plt.xlabel('Index')
plt.ylabel('TotalAmount')
plt.legend()
plt.grid(True)
plt.show()
