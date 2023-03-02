import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box


def gauss(a, b):
    a1 = a.copy()
    b1 = b.copy()
    N = len(a)

    def forward():
        for i in range(N):
            for j in range(1 + i, N):
                b[j] -= b[i] * (a[j][i] / a[i][i])
                a[j] -= a[i] * (a[j][i] / a[i][i])

    def backward():
        N = len(a)
        x = numpy.zeros(len(b), dtype=float)
        N -= 1
        x[N] = b[N] / a[N][N]

        for i in range(N - 1, -1, -1):
            x[i] = (b[i] - sum([a[i][j] * x[j] for j in range(i + 1, N + 1)])) / a[i][i]

        return x

    forward()
    print(a)
    print(b)
    x = backward()
    return x


a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))

