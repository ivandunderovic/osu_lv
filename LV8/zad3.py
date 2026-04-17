import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt
from PIL import Image

# ==============================
# 1. Učitavanje modela
# ==============================
model = keras.models.load_model("mnist_model.h5")

# ==============================
# 2. Učitavanje slike
# ==============================
img = Image.open("lv8/test.png").convert("L")  # grayscale

# prikaz originalne slike
plt.imshow(img, cmap='gray')
plt.title("Originalna slika")
plt.axis('off')
plt.show()

# ==============================
# 3. Prilagodba slike za model
# ==============================

# promjena veličine na 28x28
img = img.resize((28, 28))

# pretvorba u numpy
img_array = np.array(img)

# invertiranje (ako je pozadina bijela, a broj crn)
img_array = 255 - img_array

# skaliranje
img_array = img_array.astype("float32") / 255.0

# dodavanje dimenzija (1, 28, 28, 1)
img_array = np.expand_dims(img_array, axis=0)
img_array = np.expand_dims(img_array, axis=-1)

# ==============================
# 4. Predikcija
# ==============================
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)
confidence = np.max(prediction)

print(f"Predviđena znamenka: {predicted_class}")
print(f"Sigurnost modela: {confidence:.4f}")