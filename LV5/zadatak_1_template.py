import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . linear_model import LogisticRegression

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
plot_colors = ['r', 'b']
for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1], c=plot_colors[y[i]], marker='s')

plt.figure()

for i in range(len(X_test)):
    plt.scatter(X_test[i][0], X_test[i][1], c=plot_colors[y[i]], marker='x')
plt.show()
LogisticRegressionModel = LogisticRegression()
LogisticRegressionModel.fit(X_train, y_train)
y_test_pred = LogisticRegressionModel.predict(X_test)


plt.plot(sorted(X_test[:, 1]), LogisticRegressionModel.predict_proba(X_test)[:, 1], color='blue')
plt.show()