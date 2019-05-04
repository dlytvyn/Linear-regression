import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)


class LinearRegression:
    def __init__(self, data, args):
        if not isinstance(data, pd.DataFrame):
            raise Exception('Given data should be pandas DataFrame object')
        self.init_data = data
        self.learning_rate = args.learning_rate
        self.X = data['km'].values
        self.y = data['price'].values
        self.b0 = 0
        self.b1 = 0
        # self.y = self.y.reshape(len(self.y), 1)
        #
        # self.min_x = self.X.min(axis=0)
        # self.max_x = self.X.max(axis=0)
        #
        # self.X = ((self.X - self.X.min(axis=0)) / (self.X.max(axis=0) - self.X.min(axis=0)))
        # self.X =
        self.mean_x = np.mean(self.X)
        self.mean_y = np.mean(self.y)

    def estimate_price(self, mileage, b0, b1):
        return b0 + (b1 * mileage)

    def coefs(self):
        m = len(self.X)
        numer = 0
        demon = 0
        tmp_b0 = 0
        tmp_b1 = 0
        for i in range(m):
            tmp = tmp_b0
            tmp_b0 += self.estimate_price(self.X[i], tmp_b0, tmp_b1) - self.y[i]
            tmp_b1 += (self.estimate_price(self.X[i], tmp, tmp_b1) - self.y[i]) * self.X[i]
        self.b0 = self.learning_rate * (1 / m) * tmp_b0
        self.b1 = self.learning_rate * (1 / m) * tmp_b1

        #     numer += (self.X[i] - self.mean_x) * (self.y[i] - self.mean_y)
        #     demon += (self.X[i] - self.mean_x) ** 2
        # self.b1 = numer / demon
        # self.b0 = self.mean_y - (self.b1 * self.mean_x)

    def plot(self):
        max_x = np.max(self.X) + 100
        min_x = np.min(self.X) - 100

        x = np.linspace(min_x, max_x, 1000)
        y = self.b0 + self.b1 * x
        # line
        plt.plot(x, y, color='#58b970', label='Regression Line')
        # points
        plt.scatter(self.X, self.y, c='#ef5423', label='Scatter plot')

        plt.xlabel('Mileage in km')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def fit(self, learning_rate, accuracy):
        pass
