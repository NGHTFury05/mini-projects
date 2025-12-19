import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('population.csv')
# Display the first few rows of the dataset
print(data.head())
# Define features and target variable
X = data[['Year']]
y = data['Population']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a Linear Regression model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)
# Make predictions on the test set
y_pred = model.predict(X_test)
# Evaluate the model
r2_score = model.score(X_test, y_test)
print(f'R^2 Score: {r2_score}')
# Plot the results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth Over Years')
plt.legend()
plt.show()      