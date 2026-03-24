import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# -----------------------------
# 1. Učitavanje podataka
# -----------------------------
data = pd.read_csv(r"C:\Users\Ivan\Desktop\osulv\osu_lv\LV4\data_C02_emission.csv")

# -----------------------------
# 2. Odabir numeričkih feature-a
# -----------------------------
features = [
    "Engine Size (L)",
    "Cylinders",
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)"
]

X_numeric = data[features]
y = data["CO2 Emissions (g/km)"]

# =============================
# 3a. pd.get_dummies
# =============================
X_pd = pd.get_dummies(data[features + ["Fuel Type"]], drop_first=False)

X_train_pd, X_test_pd, y_train_pd, y_test_pd = train_test_split(X_pd, y, test_size=0.2, random_state=1)

model_pd = LinearRegression()
model_pd.fit(X_train_pd, y_train_pd)
y_pred_pd = model_pd.predict(X_test_pd)

mae_pd = mean_absolute_error(y_test_pd, y_pred_pd)
rmse_pd = mean_squared_error(y_test_pd, y_pred_pd)**0.5
r2_pd = model_pd.score(X_test_pd, y_test_pd)

print("=== Rezultati s pd.get_dummies ===")
print("MAE:", mae_pd)
print("RMSE:", rmse_pd)
print("R2:", r2_pd)

# =============================
# 3b. OneHotEncoder
# =============================
ohe = OneHotEncoder(sparse_output=False)
X_fuel_encoded = ohe.fit_transform(data[["Fuel Type"]])
fuel_cols = ohe.get_feature_names_out(["Fuel Type"])
X_fuel_encoded_df = pd.DataFrame(X_fuel_encoded, columns=fuel_cols, index=data.index)

X_ohe = pd.concat([X_numeric, X_fuel_encoded_df], axis=1)

X_train_ohe, X_test_ohe, y_train_ohe, y_test_ohe = train_test_split(X_ohe, y, test_size=0.2, random_state=1)

model_ohe = LinearRegression()
model_ohe.fit(X_train_ohe, y_train_ohe)
y_pred_ohe = model_ohe.predict(X_test_ohe)

mae_ohe = mean_absolute_error(y_test_ohe, y_pred_ohe)
rmse_ohe = mean_squared_error(y_test_ohe, y_pred_ohe)**0.5
r2_ohe = model_ohe.score(X_test_ohe, y_test_ohe)

print("\n=== Rezultati s OneHotEncoder ===")
print("MAE:", mae_ohe)
print("RMSE:", rmse_ohe)
print("R2:", r2_ohe)