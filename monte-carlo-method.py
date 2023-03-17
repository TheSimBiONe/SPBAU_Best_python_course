# Считаю интеграл от 0, до пи функции sin(x)

import random
from math import sin

right_points = 0
for _ in range(1000000):
    x = random.randrange(0, 31415) / 10000
    y = random.random()

    if sin(x) >= y:
        right_points += 1

print(right_points)
print(right_points / 1000000 * (1 * 3.1415))
# получатеся значение очень близкое к 2, которое и является ответом
