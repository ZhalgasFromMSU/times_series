def find_elipse(x, y):
    flag = False
    for i in range(3):
        if flag:
            break
        for j in range(3):
            if i == j:
                continue
            if y[i] != 0 and x[j] != 0:
                x_0, y_0 = x[i], y[i]
                x_1, y_1 = x[j], y[j]
                flag = True
                break
    if not flag:
        raise Exception('Заданные точки на одной прямой')
    a_2 = (x_1 ** 2 - (y_1 * x_0 / y_0) ** 2) / (1 - (y_1 / y_0) ** 2)
    b_2 = (y_0 ** 2 - (x_0 * y_1 / x_1) ** 2) / (1 - (x_0 / x_1) ** 2)
    print('Уравнение: x^2 / {} + y^2 / {} = 1'.format(a_2, b_2))


def find_hyper(x, y):
    flag = False
    for i in range(3):
        if flag:
            break
        for j in range(3):
            if i == j:
                continue
            if y[i] != 0 and x[j] != 0:
                x_0, y_0 = x[i], y[i]
                x_1, y_1 = x[j], y[j]
                flag = True
                break
    if not flag:
        raise Exception('По заданным точкам нельзя построить гиперболу')
    a_2 = (x_1 ** 2 - (x_0 * y_1 / y_0) ** 2) / (1 - (y_1 / y_0) ** 2)
    b_2 = (-y_0 ** 2 + (y_1 * x_0 / x_1) ** 2) / (1 - (x_0 / x_1) ** 2)
    print('Уравнение: x^2 / {} - y^2 / {} = 1'.format(a_2, b_2))


def find_parab(x, y):
    if x[0] != 0:
        p = 2 * y[0] / x[0] ** 2
    else:
        p = 2 * y[1] / x[1] ** 2
    print('Уравнение: x^2 = 2 * {} * y'.format(p))


def main():
    x = [0 for _ in range(3)]
    y = [0 for _ in range(3)]
    for i in range(3):
        x[i], y[i] = [float(cord) for cord in input('{}-я точка\n'.format(i + 1)).split()]
    curve_type = input('Тип кривой (1 - эллипс, 2 - гипербола, 3 - парабола)\n')

    try:
        if curve_type == '1':
            find_elipse(x, y)
        elif curve_type == '2':
            find_hyper(x, y)
        elif curve_type == '3':
            find_parab(x, y)
        else:
            raise Exception('Неверный тип кривой')
    except Exception as e:
        print('По заданным точкам нельзя построить кривую: ', e)


if __name__ == '__main__':
    main()

