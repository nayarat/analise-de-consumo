from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import numpy as np
import matplotlib.pyplot as plt


def regression(x, y, shape):

    model = Sequential()

    model.add(Dense(64, activation='relu', input_dim=shape))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(optimizer=RMSprop(0.001), loss='mse', metrics=['mae', 'mse'])

    model.fit(x, y, batch_size=32, epochs=1000)

    return model


numberOfTerms = 1000

y = 0.1 + np.random.rand(numberOfTerms)
t = np.linspace(0, 100, numberOfTerms)

model = regression(t, y, 1)

predictions = model.predict(t)

plt.plot(predictions, 'red')
plt.plot(y, 'blue')
plt.show()
