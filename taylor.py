from math import log

# Если нельзя было взять ваш код и изменить его под свой лад, скажите, я переделаю
# Я не нашёл как раскладывать в ряд тейлора ln(x)


def my_ln(x, iterations=200):
    """
    Вычисление натурального логарифма ln(1 + x) при помощи частичного суммирования
    ряда Тейлора для окрестности (-1, 1]
    """

    x -= 1
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(2, iterations):
        x_pow *= x  # В цикле постепенно считаем степень
        multiplier *= -1  # Домножаем на -1 для смены знака
        partial_sum += x_pow * multiplier / n

    return partial_sum


print(my_ln(2))
print(log(2))

# Выходит отличие на 2 тысячных, что на мой взгляд довольно точно
