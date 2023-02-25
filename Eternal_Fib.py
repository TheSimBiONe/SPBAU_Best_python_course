class Fib_eternal:
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _Fib_eternal_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fib1 = 1
            self.fib2 = 1

        def __next__(self):
            if self.i < 2:
                self.i += 1
                return self.fib1

            self.i += 1
            fib3 = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = fib3
            return fib3

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib_eternal._Fib_eternal_iter()


f6 = Fib_eternal()

for f in f6:
    print(f)
