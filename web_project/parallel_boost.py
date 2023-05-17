import multiprocessing
import random
from math import e, pi
from numpy import sin, cos, tan, log, exp
from numpy import linspace
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
matplotlib.use('agg')

bc = mcolors.BASE_COLORS


def monte_carlo(func, points, x_limits, y_limits, accuracy=100000):
    '''

    :param func: интегрируемая функция (подаётся в виде строки);
                 примеры: 'sin(x)' 'x ** 2'
    :param points: количество точек для подсчёта
    :param x_limits: переделы интегрирования
    :param y_limits: допустимые значения
    :param accuracy: в случае если значения будут дробными нужно указать, насколько нужно умножить
                     чтобы получились целые
    :return: значение, множество иксов, множество игриков, множество цветов
    '''

    square = (x_limits[1] - x_limits[0]) * (y_limits[1] - y_limits[0])

    points_plot_x = []
    points_plot_y = []
    points_plot_color = []

    top_right_points = 0
    bottom_right_points = 0
    x_limits = x_limits[0] * accuracy, x_limits[1] * accuracy
    y_limits = y_limits[0] * accuracy, y_limits[1] * accuracy

    for _ in range(points):
        x = random.randrange(x_limits[0], x_limits[1]) / accuracy
        y = random.randrange(y_limits[0], y_limits[1]) / accuracy

        a = eval(f'{func}')
        color = 'b'

        if a >= 0 and y >= 0:
            if a >= y:
                top_right_points += 1
                color = 'r'
        elif a < 0 and y < 0:
            if a <= y:
                bottom_right_points += 1
                color = 'r'

        points_plot_x.append(x)
        points_plot_y.append(y)
        points_plot_color.append(color)

    return (top_right_points - bottom_right_points) / points * square, \
           points_plot_x, \
           points_plot_y, \
           points_plot_color


def parallel_monte_carlo(pool, func, points, x_calc, y_calc, accuracy, tests=10):
    args = [(func, points, x_calc, y_calc, accuracy) for _ in range(tests)]
    values = [i[0] for i in pool.starmap(monte_carlo, args)]
    return sum(values) / tests


def build_plot(func, bot_top, x, y, colors):

    '''
    Функция строит график по результатам работы функции monte_carlo

    :param func: функция для построения
    :param bot_top: пределы построения функции по иксу
    :param x: множество иксов (результат работы monte_carlo)
    :param y: множество игриков (результат работы monte_carlo)
    :param colors: множество цветов (результат работы monte_carlo)
    :return:
    '''

    # with используется чтобы сделать оси графика и цифры на нихбеленьким
    with plt.rc_context({'axes.edgecolor': 'white', 'xtick.color': 'white', 'ytick.color': 'white'}):
        ax = plt.axes()
        ax.grid(which='major', alpha=1)

        plt.scatter(x, y, s=1, c=colors)

        x = linspace(bot_top[0], bot_top[1])
        plt.plot(x, eval(f'{func}'), color='green')

        # plt.show()
        plt.savefig('static/plot.png', dpi=500, bbox_inches='tight', transparent=True)

        # Очищение графика для следующего интеграла
        plt.clf()


if __name__ == '__main__':
    poool = multiprocessing.Pool()
    print(parallel_monte_carlo(poool, 'sin(x)', 1000000, (0, 2 * 3.1415), (-1, 1), 10000))
