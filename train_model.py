# train_model.py
# ------------------------------------------
# Train and save Linear Regression pipeline for Salary Prediction using pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# 1️⃣ Load dataset
data = pd.read_csv("Salary_dataset.csv")

print("✅ Dataset loaded successfully!")
print(data.head())

# 2️⃣ Define features and target
X = data[['YearsExperience']]
y = data['Salary']

# 3️⃣ Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Build pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

# 5️⃣ Train model
pipeline.fit(X_train, y_train)

# 6️⃣ Evaluate model
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Performance:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 7️⃣ Save model using pickle
with open("salary_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("\n💾 Model saved successfully as 'salary_model.pkl'")
