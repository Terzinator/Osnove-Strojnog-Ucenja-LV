import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

model = keras.models.load_model('FCN_model.keras')

y_pred = model.predict(x_test_s)

print(y_test[12])
print(y_pred[12])

for i in range(len(x_test_s)):
    if(y_test_s[i] != y_pred[i]):
        plt.imshow(x_train[i])
        plt.title(y_train[i])
        plt.show()
