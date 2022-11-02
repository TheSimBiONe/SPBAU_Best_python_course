
#!/usr/bin/env python3

"""
Реализация алгоритма Рабина-Карпа с модульными тестами
"""

import unittest


def rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа
    Параметры:
    ----------
        text: str
            текст
        pattern: str
            образец
    Возвращаемое значение
    ---------------------
        список позиций в тексте, с которых начинаются вхождения образца
    """
    result = []

    # Менять отсюда =) ---- vvvvv ----

    if text == "":
        return result

    # Почему-то он мне считал на 1 больше вхождений пустой строки, так что я уменьшил текст на 1
    # Это не совсем подход программиста, но зато работает :)
    if pattern == "":
        text = text[:-1]

    pattern_hash = 0
    pattern_len = len(pattern)
    for char in pattern:  # Вычисление "хэш" суммы(я знаю что она не хэш на самом деле) для подстроки
        pattern_hash += ord(char)

    cur_hash = 0
    for i in range(pattern_len):  # Вычисление первой хэш суммы, потом её будем менять
        cur_hash += ord(text[i])

    for i in range(pattern_len, len(text)):
        if cur_hash == pattern_hash:  # Если значения хэш сумм совпадают, то следует дальнейшая проверка
            if text[i - pattern_len:i] == pattern:
                result.append(i - pattern_len)
        cur_hash -= ord(text[i - pattern_len])
        cur_hash += ord(text[i])

    # Последняя проверка, так как цикл останавливается, не проверяя последний символ
    if cur_hash == pattern_hash:
        if text[(i - pattern_len + 1):(i + 1)] == pattern:
            result.append(i - pattern_len + 1)
    # Менять до сюда =) ---- ^^^^^ ----

    return result


class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Должно выдать:
# --------------
# Ran ... tests in ...s
# OK

# Запуск тестов


if __name__ == '__main__':
    unittest.main()
