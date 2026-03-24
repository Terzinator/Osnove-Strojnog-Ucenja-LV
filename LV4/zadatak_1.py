import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error


data = pd.read_csv('data_C02_emission.csv')

data = data._get_numeric_data()

X = data.iloc[: ,0:5]
y = data.iloc[: ,6]

X_train , X_test , y_train , y_test = train_test_split (X, y, test_size = 0.2, random_state =1)

plt.scatter(X_train.iloc[: , 2], y_train, color='blue')
plt.scatter(X_test.iloc[: , 2], y_test, color='red')
plt.show()

plt.hist(X_train.iloc[: , 2], color='red')

sc = MinMaxScaler ()
X_train_n = sc.fit_transform(X_train)

plt.figure()
plt.hist(X_train_n[: , 2], color='green')

plt.show()

X_test_n = sc.transform(X_test)

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n ,y_train)

coefficients = linearModel.coef_
zero_coefficient = linearModel.intercept_
print(zero_coefficient)
for i in range(len(coefficients)):
    print(f"+{coefficients[i]}*x{i+1}")

y_test_p = linearModel.predict(X_test_n)


plt.figure()
plt.scatter(y_test_p, y_test, color='green')
plt.xlabel("Predicted Values")
plt.ylabel("Real Values")
plt.show