import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_3.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()


# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transformiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

km = KMeans(n_clusters=5, random_state=0).fit(img_array)
labels = km.predict(img_array)
num_colors =len(np.unique(img_array))
print("Broj boja u slici: ", num_colors/3)
# rezultatna slika

result_image = np.zeros((w,h,d))

label_index = 0

for i in range(w):
    for j in range(h):
        result_image[i][j] = km.cluster_centers_[labels[label_index]]
        label_index += 1

new_num_colors =len(np.unique(result_image))
print("Broj boja u rezultatnoj slici: ", new_num_colors/3)
plt.figure()
plt.title("Rezultatna slika")
plt.imshow(result_image)
plt.tight_layout()
plt.show()
