import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv('population.csv')
X = data[['Year']]
y = data['Population']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2_score = model.score(X_test, y_test)
print(f'R^2 Score: {r2_score}')
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth Over Years')
plt.legend()
plt.show()  
joblib.dump(model, 'linear_regression_model.pkl')  
print("Model saved as 'linear_regression_model.pkl'")
  