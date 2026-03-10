import numpy as np
import matplotlib.pyplot as plt

# koordinate točaka sa slike
x = np.array([1.0, 2.0, 3.0, 3.0, 1.0])
y = np.array([1.0, 2.0, 2.0, 1.0, 1.0])


plt.plot(x, y, 'b', linewidth=2, marker='.', markersize=8)


plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Zad1')

# raspon osi
plt.xlim(0.0, 4.0)
plt.ylim(0.0, 4.0)

plt.show()
