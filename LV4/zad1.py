import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# -----------------------------
# a) Učitavanje podataka
# -----------------------------
data = pd.read_csv(r"C:\Users\Ivan\Desktop\osulv\osu_lv\LV4\data_C02_emission.csv")

# odabir numeričkih stupaca
features = [
    "Engine Size (L)",
    "Cylinders",
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)"
]

target = "CO2 Emissions (g/km)"

X = data[features]
y = data[target]

# podjela 80-20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# -----------------------------
# b) Scatter plot
# -----------------------------
plt.figure()
plt.scatter(X_train["Engine Size (L)"], y_train, color="blue", label="Train")
plt.scatter(X_test["Engine Size (L)"], y_test, color="red", label="Test")
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.title("CO2 vs Engine Size")
plt.show()

# -----------------------------
# c) Standardizacija,  StandardScaler: transformira podatke tako da imaju sredinu 0 i std devijaciju 1
# -----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


plt.figure()
plt.hist(X_train["Engine Size (L)"], bins=20)
plt.title("Histogram prije skaliranja")
plt.xlabel("Engine Size (L)")
plt.ylabel("Frekvencija")
plt.show()


plt.figure()
plt.hist(X_train_scaled[:, 0], bins=20)
plt.title("Histogram nakon skaliranja")
plt.xlabel("Standardizirane vrijednosti")
plt.ylabel("Frekvencija")
plt.show()


for i, feature in enumerate(features):
    plt.figure(figsize=(10,4))

    # prije skaliranja
    plt.subplot(1, 2, 1)
    plt.hist(X_train[feature], bins=20)
    plt.title(f"{feature} - prije skaliranja")
    plt.xlabel(feature)
    plt.ylabel("Frekvencija")

    # nakon skaliranja
    plt.subplot(1, 2, 2)
    plt.hist(X_train_scaled[:, i], bins=20)
    plt.title(f"{feature} - nakon skaliranja")
    plt.xlabel("Standardizirane vrijednosti")
    plt.ylabel("Frekvencija")

    plt.tight_layout()
    plt.show()


# -----------------------------
# d) Linearna regresija, uci koeficijente da moze kasnije samo sa x i tim koeficijentima odredit y, presjek je kad  su svi keof 0 
# -----------------------------
model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("Koeficijenti:", model.coef_)
print("Presjek (bias):", model.intercept_)

# -----------------------------
# e) Predikcija i scatter
# -----------------------------
y_pred = model.predict(X_test_scaled)

plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Stvarne vrijednosti CO2")
plt.ylabel("Predikcije CO2")
plt.title("Stvarno vs Predviđeno")
plt.show()

# -----------------------------
# f) Evaluacija
# -----------------------------
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R2:", r2)



feature_sets = [
    ["Engine Size (L)"],
    ["Engine Size (L)", "Cylinders"],
    ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)"],
    ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)"],
    ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)"]
]

print("\n=== Usporedba modela s različitim brojem varijabli ===")

for i, feat_set in enumerate(feature_sets):
    X_temp = data[feat_set]

    X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
        X_temp, y, test_size=0.2, random_state=1
    )

    scaler_t = StandardScaler()
    X_train_t = scaler_t.fit_transform(X_train_t)
    X_test_t = scaler_t.transform(X_test_t)

    model_t = LinearRegression()
    model_t.fit(X_train_t, y_train_t)

    y_pred_t = model_t.predict(X_test_t)

    mse_t = mean_squared_error(y_test_t, y_pred_t)
    rmse_t = np.sqrt(mse_t)
    mae_t = mean_absolute_error(y_test_t, y_pred_t)
    r2_t = r2_score(y_test_t, y_pred_t)

    print(f"\nModel {i+1} - broj varijabli: {len(feat_set)}")
    print("Varijable:", feat_set)
    print("MSE:", mse_t)
    print("RMSE:", rmse_t)
    print("MAE:", mae_t)
    print("R2:", r2_t)
    
# -----------------------------
# g) Napomena
# -----------------------------
print("\nNapomena:")
print("Povećanjem broja ulaznih varijabli model obično bolje uči (manja greška),")
print("ali može doći do overfittinga ako ih ima previše.")