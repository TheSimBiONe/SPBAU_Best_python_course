import multiprocessing
import random
import math


def monte_carlo(func, points, x_limits, y_limits, accuracy=1):
    '''

    :param func: интегрируемая функция
    :param points: количество точек для посчёта
    :param x_limits: переделы интегрирования
    :param y_limits: допустимые значения
    :param accuracy: в случае если значения будут добными нужно указать, насколько нужно умножить
                     чтобы получились целые
    :return:
    '''

    square = (x_limits[1] - x_limits[0]) * (y_limits[1] - y_limits[0])

    top_right_points = 0
    bottom_right_points = 0
    x_limits = x_limits[0] * accuracy, x_limits[1] * accuracy
    y_limits = y_limits[0] * accuracy, y_limits[1] * accuracy

    for _ in range(points):
        x = random.randrange(x_limits[0], x_limits[1]) / accuracy
        y = random.randrange(y_limits[0], y_limits[1]) / accuracy

        a = func(x)
        if a >= 0 and y >= 0:
            if a >= y:
                top_right_points += 1
        elif a < 0 and y < 0:
            if a <= y:
                bottom_right_points += 1

    return top_right_points / points * square - bottom_right_points / points * square


def parallel_monte_carlo(pool, func, points, x_calc, y_calc, accuracy, tests=10):
    args = [(func, points, x_calc, y_calc, accuracy) for _ in range(tests)]
    return sum(pool.starmap(monte_carlo, args)) / tests


if __name__ == '__main__':
    poool = multiprocessing.Pool()
    print(parallel_monte_carlo(poool, math.sin, 1000000, (0, 2 * 3.1415), (-1, 1), 10000))
else:
    print("__name__:", __name__)