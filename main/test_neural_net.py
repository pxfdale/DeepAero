import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) # Add parent directory to path
from modules.generate_sample import generate_sample
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create model
model = Sequential()

model.add(Dense(1600, activation='relu', input_shape=(1600,)))
model.add(Dropout(0.3))

model.add(Dense(500, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(100, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(50, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(26))

# Compile model (required to make predictions)
model.compile(loss='mse', optimizer='adam')

# load weights
model.load_weights("model.h5")

# Generate sample
X, y = generate_sample()
X = np.array(X).reshape((1, 1600))
y = np.array(y).reshape((1, 26))

# estimate accuracy on whole dataset using loaded weights
loss = model.evaluate(X, y)
prediction = model.predict(X)

# Visualization
data = {'Real': y[0, :].tolist(), 'Predict': prediction[0, :].tolist()}
df = pd.DataFrame(data)
print('{}: {}'.format(model.metrics_names, loss))
print(df.round(5))


