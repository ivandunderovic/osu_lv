import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Ivan\Desktop\osulv\osu_lv\LV3\data_C02_emission.csv")

#a
plt.figure()
plt.hist(df["CO2 Emissions (g/km)"], bins=20, edgecolor="black")
plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Broj vozila")
plt.title("Histogram CO2 emisije")
plt.show()


#b
plt.figure()

colors = df["Fuel Type"].astype("category").cat.codes

plt.scatter(df["Fuel Consumption City (L/100km)"],
            df["CO2 Emissions (g/km)"],
            c=colors)

plt.xlabel("Fuel Consumption City (L/100km)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Odnos gradske potrošnje i CO2 emisije")

plt.show()

#c
plt.figure()

df.boxplot(column="Fuel Consumption Hwy (L/100km)", by="Fuel Type")

plt.title("Izvangradska potrošnja po tipu goriva")
plt.suptitle("")
plt.xlabel("Fuel Type")
plt.ylabel("Fuel Consumption Hwy (L/100km)")

plt.show()

#d
fuel_counts = df.groupby("Fuel Type").size()

plt.figure()
fuel_counts.plot(kind="bar")

plt.xlabel("Fuel Type")
plt.ylabel("Broj vozila")
plt.title("Broj vozila po tipu goriva")

plt.show()


#e
avg_co2 = df.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()

plt.figure()
avg_co2.plot(kind="bar")

plt.xlabel("Broj cilindara")
plt.ylabel("Prosječna CO2 emisija (g/km)")
plt.title("Prosječna CO2 emisija s obzirom na broj cilindara")

plt.show()