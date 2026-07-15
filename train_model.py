import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


# Load dataset
df = pd.read_csv("dataset/customer_data.csv")

print("COLUMNS FOUND:", df.columns.tolist())


# Features
X = df[
    [
        "tenure",
        "monthly_charges",
        "total_charges",
        "satisfaction_score"
    ]
]


# Target
y = df["clv"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Predict
y_pred = model.predict(X_test)


# Evaluate model
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)


print("\nModel Performance")
print("------------------")
print("R2 Score:", round(r2, 3))
print("Mean Absolute Error:", round(mae, 2))


# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("\nModel trained and saved as model.pkl")