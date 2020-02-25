# Найти размерность вложения для ряда полученного из пробега по эллипсу
from math import sin, cos, log
from scipy.spatial.distance import euclidean as dist
from numpy.linalg import norm


dt = 0.01  # Дэльта времени
N = 1000   # Количество элементов в ряду
L = 0.01    # Размер расстояния значимости

A = 5       # Большая полуось эллипса
B = 3       # Малая полуось эллипса


def distance(w_1, w_2):
    return norm([dist(i, j) for i, j in zip(w_1, w_2)])


def init_series():
    return [(A * cos(i * dt), B * sin(i * dt)) for i in range(N)]


def find_corel_size(t_s, k):
    ret = 0
    for i in range(k, N):
        if i % 100 == 0:
            print(ret, i)
        ret += 1
        for j in range(i + 1, N):
            ret += 2 * (L >= distance(t_s[i - k:i + 1], t_s[j - k:j + 1]))
    return log(ret / (N - k) ** 2) / log(L)

def main(time_series):
    prev = None
    for k in range(1, 10):
        cur = find_corel_size(time_series, k)
        print(cur)
        if prev == cur:
            print('Found:', k)
            return
        prev = cur


if __name__ == '__main__':
    main(init_series())
