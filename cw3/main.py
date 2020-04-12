import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def la(data, p, second_order=True, eps=1e-5):
    Xi = 3 * (p + 1)
    X = data[np.arange(p) + np.arange(len(data) - p)[:, np.newaxis]]
    omega = np.argpartition(np.sum(np.power(X - data[-p:], 2), axis=1), Xi)[:Xi]
    if not second_order:
        Y = np.hstack((np.ones(Xi)[:, None], X[omega]))
    else:
        idx = np.arange(p)[:, None] - np.arange(p) <= 0
        Y = np.hstack((np.ones(Xi)[:, None], (X[omega, :, None] * X[omega, None, :])[:, idx]))
    params = np.linalg.solve(Y.T @ Y + eps * np.eye(Y.shape[1]), Y.T @ data[omega + p])
    if not second_order:
        return params, np.sum(params * np.hstack([1, data[-p:]]))
    else:
        return params, np.sum(params * np.hstack([1, (data[-p:, None] * data[-p:])[idx]]))


def main(data):
    data = np.array(data.cost)
    for i in range(len(data) // 4):
        data = np.append(data, la(data, 30, False)[1])
    return data


if __name__ == '__main__':
    plt.plot(main(pd.read_csv('data.csv', delimiter=';', names=['date', 'cost'])))
    plt.show()
