import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("road.jpg")
img = img [:,:,0]. copy ()

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

plt.figure()
plt.imshow(img, cmap="gray", vmax=100)
plt.show()

plt.figure()
plt.imshow(np.flip(img), cmap="gray")
plt.show()

