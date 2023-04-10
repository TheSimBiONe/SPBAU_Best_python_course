import multiprocessing
import random
import math


def monte_carlo(func, points, x_limits, y_limits, accuracy=1):
    '''

    :param func: интегрируемая функция
    :param points: количество точек для посчёта
    :param x_limits: переделы интегрирования умноженные на accuracy
    :param y_limits: допустимые значения умноженные на accuracy
    :param accuracy: в случае если значения будут добными нужно указать до какого знака,
    :return:
    '''

    square = (x_limits[1] - x_limits[0]) * (y_limits[1] - y_limits[0])

    right_points = 0
    x_limits = x_limits[0] * accuracy, x_limits[1] * accuracy
    y_limits = y_limits[0] * accuracy, y_limits[1] * accuracy

    for _ in range(points):
        x = random.randrange(x_limits[0], x_limits[1]) / accuracy
        y = random.randrange(y_limits[0], y_limits[1]) / accuracy

        if func(x) >= y:
            right_points += 1

    return right_points / points * square


def parallel_monte_carlo(pool, func, points, x_calc, y_calc, accuracy, tests=20):
    args = [(func, points, x_calc, y_calc, accuracy) for _ in range(tests)]
    return sum(pool.starmap(monte_carlo, args)) / tests


if __name__ == '__main__':
    poool = multiprocessing.Pool()
    print(parallel_monte_carlo(poool, math.sin, 1000000, (0, 3.1415), (0, 1), 10000))
else:
    print("__name__:", __name__)