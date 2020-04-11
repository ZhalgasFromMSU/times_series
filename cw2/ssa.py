import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def main(data):
    tau = (1 + len(data)) // 4
    X_T = np.array([data.cost[i:i + tau] for i in range(len(data) - tau + 1)])
    cov_mat = np.dot(X_T.T, X_T) / len(data)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    Y = np.dot(eig_vecs.T, X_T.T)

    r = (1 + len(data)) // 16
    X_new = np.dot(eig_vecs[:, :r], Y[:r])

    tmp_X = np.fliplr(X_new)
    cost_smoth = np.array([np.mean(tmp_X.diagonal(tmp_X.shape[1] - 1 - i)) for i in range(len(data))])

    eig_vecs_ast = eig_vecs[:tau - 1, :r]
    eig_vecs_tau = eig_vecs[-1, :r]
    Q = X_T[-1, 1:]

    res = np.array(data.cost)
    p = len(data) // 4
    for i in range(p):
        x_new = np.dot(np.dot(eig_vecs_tau, eig_vecs_ast.T), Q) / (1 - np.dot(eig_vecs_tau, eig_vecs_tau.T))
        res = np.append(res, x_new)
        Q = np.append(Q, x_new)[1:]
    return res


if __name__ == '__main__':
    plt.plot(main(pd.read_csv('data.csv', delimiter=';', names=['date', 'cost'])))
    plt.show()
