import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', dtype=None, names=True, encoding=None)

print("Number of participants:", len(data))

height = []
weight = []

for i in range(len(data)):
    height.append(data[i][1])
    weight.append(data[i][2])

heightArray = np.array(height)
weightArray = np.array(weight)

h = heightArray[::50]
w = weightArray[::50]

plt.scatter(heightArray, weightArray)
plt.scatter(h, w)
plt.show()

print("MinHeight:",heightArray.min(),"MaxHeight:", heightArray.max(), "AverageHeight:", heightArray.mean())

heightMale = []
weightMale = []
heightFemale = []
weightFemale = []

for i in range(len(data)):
    if(data[i][0] == 1):
        heightMale.append(data[i][1])
        weightMale.append(data[i][2])
    else:
        heightFemale.append(data[i][1])
        weightFemale.append(data[i][2])

heightMaleArray = np.array(heightMale)
weightMaleArray = np.array(weightMale)
heightFemaleArray = np.array(heightFemale)
weightFemaleArray = np.array(weightFemale)

print("Male stats","MinHeight:",heightMaleArray.min(),"MaxHeight:", heightMaleArray.max(), "AverageHeight:", heightMaleArray.mean())

print("Female stats","MinHeight:",heightFemaleArray.min(),"MaxHeight:", heightFemaleArray.max(), "AverageHeight:", heightFemaleArray.mean())