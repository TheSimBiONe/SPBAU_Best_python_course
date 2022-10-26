import turtle as tl


def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 3.0)
        t1.left(100)
        draw_fractal(scale / 3.0)
        t1.right(80)
        draw_fractal(scale / 3.0)
        t1.right(80)
        draw_fractal(scale / 3.0)
        t1.left(100)
        draw_fractal(scale / 3.0)
    else:
        t1.forward(scale)


scale = 400

t1 = tl.Turtle()  # Создаём черепашку
t1.pensize(2)  # Делаем линию рисования по толше
t1.penup()  # Поднимаем перо (чтобы оно не рисовало
t1.goto(0, -50)  # Двигаем черепашку
t1.pendown()  # Опускаем перо

draw_fractal(scale)
draw_fractal(scale)
draw_fractal(scale)
# Рисуем фрактал 3 раза, чтобы он замкнулся
# Он рисуется довольно долго но резутат получется красивым

tl.done()

