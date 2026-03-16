import pandas as pd

df = pd.read_csv(r"C:\Users\Ivan\Desktop\osulv\osu_lv\LV3\data_C02_emission.csv")

#a
print("Broj mjerenja:", df.shape[0])

print("\nTipovi podataka:")
print(df.dtypes)

print("\nNedostajuće vrijednosti:")
print(df.isnull().sum())

print("\nDuplicirani redovi:", df.duplicated().sum())

df = df.dropna()
df = df.drop_duplicates()

categorical_cols = ["Make","Model","Vehicle Class","Transmission","Fuel Type"]
for col in categorical_cols:
    df[col] = df[col].astype("category")

print("\nTipovi nakon konverzije:")
print(df.dtypes)


#b
print("\n3 vozila s najvećom gradskom potrošnjom:")
print(df.nlargest(3, "Fuel Consumption City (L/100km)")[["Make","Model","Fuel Consumption City (L/100km)"]])

print("\n3 vozila s najmanjom gradskom potrošnjom:")
print(df.nsmallest(3, "Fuel Consumption City (L/100km)")[["Make","Model","Fuel Consumption City (L/100km)"]])

#c
filtered = df[(df["Engine Size (L)"] >= 2.5) & (df["Engine Size (L)"] <= 3.5)]

print("\nBroj vozila (2.5–3.5 L):", filtered.shape[0])
print("Prosječna CO2 emisija:", filtered["CO2 Emissions (g/km)"].mean())


#d
audi = df[df["Make"] == "Audi"]

print("\nBroj Audi vozila:", audi.shape[0])

audi4 = audi[audi["Cylinders"] == 4]
print("Prosječna CO2 emisija Audi vozila s 4 cilindra:",
      audi4["CO2 Emissions (g/km)"].mean())


#e
print("\nBroj vozila po cilindrima:")
print(df["Cylinders"].value_counts())

print("\nProsječna CO2 emisija po cilindrima:")
print(df.groupby("Cylinders")["CO2 Emissions (g/km)"].mean())


#f
diesel = df[df["Fuel Type"] == "D"]
regular = df[df["Fuel Type"] == "X"]

print("\nDizel:")
print("Prosjek gradske potrošnje:",
      diesel["Fuel Consumption City (L/100km)"].mean())
print("Medijan:",
      diesel["Fuel Consumption City (L/100km)"].median())

print("\nRegular benzin:")
print("Prosjek gradske potrošnje:",
      regular["Fuel Consumption City (L/100km)"].mean())
print("Medijan:",
      regular["Fuel Consumption City (L/100km)"].median())


#g
diesel4 = df[(df["Fuel Type"] == "D") & (df["Cylinders"] == 4)]

car = diesel4.loc[diesel4["Fuel Consumption City (L/100km)"].idxmax()]

print("\nDizel vozilo s 4 cilindra s najvećom potrošnjom:")
print(car[["Make","Model","Fuel Consumption City (L/100km)"]])


#h
manual = df[df["Transmission"].str.contains("M")]

print("\nBroj vozila s ručnim mjenjačem:", manual.shape[0])

#i
corr = df.corr(numeric_only=True)

print("\nKorelacija numeričkih varijabli:")
print(corr)