import sys

from math import sin, cos


def init_series(N, dt, A, B):
    return [(float(A) * cos(i * float(dt)), float(B) * sin(i * float(dt))) for i in range(int(N))]


if __name__ == '__main__':
    for x, y in init_series(*sys.argv[1:]):
        print(x, y, end=' ')
    print()
