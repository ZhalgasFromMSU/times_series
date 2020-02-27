import sys

from math import log


def main():
    N, l, CAP = sys.argv[1:]
    for i in range(1, int(CAP)):
        k, num = [int(i) for i in input().split()]
        print(log(num / (int(N) - k) ** 2) / log(float(l)))


if __name__ == '__main__':
    main()
