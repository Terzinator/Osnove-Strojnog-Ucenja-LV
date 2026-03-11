import matplotlib.pyplot as plt
import numpy as np

a = np.array([[1.0, 2.0], [1.0, 2.0]])
b = np.array([[2.0, 3.0], [2.0, 2.0]])
c = np.array([[3.0, 3.0], [2.0, 1.0]])
d = np.array([[1.0, 3.0], [1.0, 1.0]])

plt.axis([0.0, 4.0, 0.0, 4.0])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Zadatak 1")
plt.plot(a[0], a[1], color='g')
plt.plot(b[0], b[1], color='g')
plt.plot(c[0], c[1], color='g')
plt.plot(d[0], d[1], color='g')
plt.show()
