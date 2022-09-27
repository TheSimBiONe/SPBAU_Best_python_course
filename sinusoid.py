#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Подключение модулей
import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # Тело условия не выполнится в случае,
    # если файл будет импортирован
    arguments = numpy.arange(0, 200, 0.1)  # Создание массива аргументов
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
        # Создание объекта типа "график"
    )
    mpp.show()  # Вывод графика на экран
