def euclid(a, b):
    '''
    Возвращает наибольший общий делитель двух чисел
    a >= b >= 0

    :param a:
    :param b:
    :return:
    '''

    if b == 0:
        return a
    return euclid(b, a % b)


def ext_euclid(a, b):
    '''
    Возвращает наибольший общий делитель двух чисел
    a >= b >= 0

    :param a:
    :param b:
    :return:
    '''

    if b == 0:
        return 1, 0, a
    x, y, d = ext_euclid(b, a % b)
    return y, x - int(a / b) * y, d


class Test_func():
    def __init__(self, tests, func):
        self.tests = tests
        self.func = func
        self.results = []

    def check(self, condition_cheked=lambda x, y, z: y == z):
        '''
        Метод выполняет проверку возрщаемых значений функции

        Параметр этого метода нуже для тех случаев, когда для корректности недостаточно лишь
        сравнить возвращаемое значение. Можно задавать корректность работы, выполнением некоторого
        условия, которое описывается с помощью вводимых, выводимых значений функции и то
        с чем нужно сравнивать вывод

        :param condition_cheked:
        :return:
        '''
        self.results.clear()
        for test in self.tests:
            returned = self.func(*test[0])
            self.results.append((test[0], returned,
                                 condition_cheked(test[0], returned, test[1])))

    def print_result(self):
        '''
        Метод печатает в консоль результаты тестов

        :return:
        '''

        count = 1
        print('Testing start\n'
              f'function: {self.func.__name__}\n')
        for result in self.results:
            if result[2] == 0:
                print(f'Test {count}: '
                      f'input: {result[0]}\n'
                      f'returned: {result[1]}\n'
                      f'correctness: Fail\n')
            else:
                print(f'Test {count}: '
                      f'input: {result[0]}\n'
                      f'returned: {result[1]}\n'
                      f'correctness: Done\n')
            count += 1
        print('Testing finished\n')


tests = [((1, 0), 1),
         ((5, 3), 1),
         ((92, 69), 23),
         ((108026161, 19637473), 311)]

euclid_test = Test_func(tests, euclid)
euclid_test.check()
euclid_test.print_result()

# Тут я использую фишку класса который написал. Вместо того чтобы записывать коэффициенты в тесты, я
# проверяю что они удволетворяют условию. Таких коэффициентов бесконенчо много, а какие программа
# выдаст, я не знаю))
ext_euclid_test = Test_func(tests, ext_euclid)
ext_euclid_test.check(lambda x, y, z: x[0] * y[0] + x[1] * y[1] == z == y[2])
ext_euclid_test.print_result()
