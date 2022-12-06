# Далее под перестановкой я имею ввиду сокращённою табличную запись перестановки
# А под элементом симметрической группы - собственно перестановку

# P.S. Алгоритм сортировки слиянием был нагло украден с википедии и доработан мною для моих целей
# Как оказалось ей хорошо решается поиск инверсий


def cycle_from_permutation(σ, begin, cycle):
    '''
    Находит цикл из σ в который входит элемент begin.

    :param σ: Перестановка
    :param begin: Один из элементов
    :param cycle: Нужна для возврата цикла
    :return:
    '''
    if begin in cycle:
        return begin
    cycle.append(begin)
    cycle_from_permutation(σ, σ[begin - 1], cycle)
    return cycle


def merge_sort_with_inversions(A, invert = 0):
    '''
    :param A: Сортируемый список
    :param invert: Текущее количество инверсий
    :return: Отсортированный список, количество инверсий в исходном списке
    '''
    if len(A) == 1 or len(A) == 0:
        return A, invert
    L, invL = merge_sort_with_inversions(A[:len(A) // 2])
    R, invR = merge_sort_with_inversions(A[len(A) // 2:])
    inversions = invL + invR
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            inversions += len(L) - n
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        inversions += len(L) - n
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A, inversions


class Permutation:
    def __init__(self, permutation=[]):
        '''
        Класс элемента симметрической группы, задаётся в виде перестановки или произведения
        непересекающихся циклов. Если используется последний способ, то в конце нужно указать
        длинну перестановки. Если не передать аргументов, объект будет считаться тождественной
        перестановкой.

        :param permutation: [a, b, c, .., d] или ['(a b .. c)(d e .. f)..(g h .. i)',  кол-во эл]
        '''

        self.cycles = []  # Разложение перестановки в циклы
        self.permutation = []  # Перестановка
        self.id = False  # С тождестенной перестановкой будем работать подругому
        self.inversions = 0

        try:
            if len(permutation) == 0:
                self.id = True

            elif type(permutation[0]) == int:  # Если мы передаём как перестановку, то находим циклы
                self.permutation = list(permutation)
                self._solve_cycles()
                self.id = self._is_id()
                self.inversions = merge_sort_with_inversions(self.permutation)[1]

            elif type(permutation[0]) == str:  # Если мы передаём как циклы, то находим перестановку
                self.cycles = [list(map(int, cycle[:-1].split())) for cycle in permutation[0].split('(')[1:]]
                self.permutation = [i + 1 for i in range(permutation[-1])]
                self._solve_permutation()
                self.id = self._is_id()
                self.inversions = merge_sort_with_inversions(self.permutation)[1]
        except IndexError:
            pass

    def _solve_cycles(self):
        '''
        Находит на основании self.permutation разложение в циклы для self.cycles
        '''

        permutation1 = self.permutation.copy()
        self.cycles.clear()
        while permutation1:
            self.cycles.append(cycle_from_permutation(self.permutation, permutation1[0], []))
            for i in self.cycles[-1]:
                permutation1.remove(i)  # Удаление элемента, кототрый уже есть в одном из циклов

    def _solve_permutation(self):
        '''
        Находит на основании self.cycles перестановку для self.permutation
        '''

        for cycle in reversed(self.cycles):
            l = len(cycle)
            for i in range(l):
                self.permutation[cycle[i] - 1] = cycle[(i + 1) % l]

    def __str__(self):
        '''
        Печатает в консоль перестановку если вызвать print.
        '''

        if self.id:
            return 'id'
        return f"({', '.join(list(map(str, tuple(self.permutation))))})"

    def print_cycles(self):
        '''
        Печатает в консоль произведение непересекющихся циклов.
        '''

        if self.id:
            print('id')
        else:
            print(''.join([f"({' '.join(list(map(str, cycle)))})" for cycle in self.cycles if len(cycle) > 1]))

    def _is_id(self):
        '''
        :return: True если перестановка тождественная, False если нет. Атрибут self.id хранит
        аналогичное значение.
        '''

        for i in range(len(self.permutation)):
            if i + 1 != self.permutation[i]:
                return False

        self.permutation = [1]
        self.cycles = [1]

        return True

    def __eq__(self, other):
        try:
            if self.permutation == other.permutation:
                return True
        except AttributeError:  # Если сравниваем с объектом не класса Permutation, то вернём False
            return False
        return False

    def __mul__(self, other):
        '''
        Метод считает композицию двух элементов симметрической группы.
        Как и в алгебре первая применяется перестановка, которая справа.

        :param other: Экземпляр класса Permutation
        :return: Композиция двух элементов симметической подгруппы
        '''

        if type(other) != Permutation:
            raise TypeError("unsupported operand type(s) for *: 'Permutation' and 'int'")

        if self.id:
            return Permutation(other.permutation)
        elif other.id:
            return Permutation(self.permutation)

        result = []
        l = max(len(self.permutation), len(other.permutation))

        # Исключения нужны, чтобы обработать умножение перестановок, которые могут не лежать в одной
        # симметрической группе.
        for i in range(1, l + 1):
            try:
                result.append(self.permutation[other.permutation[i - 1] - 1])
            except IndexError:
                try:
                    result.append(other.permutation[i - 1])
                except IndexError:
                    result.append(self.permutation[i - 1])

        return Permutation(result)

    def __neg__(self):
        '''
        :return: Обратный элемент к элементу симметрической группы.
        '''

        result = []
        for i in range(1, len(self.permutation) + 1):
            result.append(self.permutation.index(i) + 1)

        return Permutation(result)

    def __invert__(self):
        '''
        :return: Возвращает количество инверсий в перестановке
        '''
        return self.inversions


# оставлю тут несколько экзепляров для того, чтобы посмотреть, как они работают
if __name__ == '__main__':
    a = Permutation([4, 3, 1, 2, 6, 7, 5])
    b = Permutation([3, 2, 4, 5, 1])
    c = Permutation([6, 3, 2, 5, 4, 1])

    print(~a)
