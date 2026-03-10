import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt( "osu_lv/LV2/data.csv", delimiter=",", skiprows=1 )

print("Broj osoba:", data.shape[0])

visina = data[:, 1]
masa = data[:, 2]

plt.scatter(visina, masa)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Odnos visine i mase")
plt.show()

plt.scatter(visina[::50], masa[::50])
plt.show()

print("Minimalna visina:", np.min(visina))
print("Maksimalna visina:", np.max(visina))
print("Srednja visina:", np.mean(visina))

muskarci = data[data[:, 0] == 1]

visina_m = muskarci[:, 1]

print("Minimalna visina muskarci:", np.min(visina_m))
print("Maksimalna visina muskarci:", np.max(visina_m))
print("Srednja visina muskarci:", np.mean(visina_m))

zene = data[data[:, 0] == 0]
visina_z = zene[:, 1]

print("Minimalna visina žene:", np.min(visina_z))
print("Maksimalna visina žene:", np.max(visina_z))
print("Srednja visina žene:", np.mean(visina_z))
