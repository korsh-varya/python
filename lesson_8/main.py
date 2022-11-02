#Первый способ импортирования
# import random
#print(random.randint(0,100))

#второй способ импортирования
# import random as r
# print(r.randint(0,100))
#
# from random import randint
# print(randint(0,100))

# from random import *   #лучше не надо(импортировать все не подсказывает функции)
# print(randint(0,100))

# import random as r
# lst = [1,2,3,4,5]
# print(r.choice(lst))
# r.shuffle(lst)         # перемешать содержимое
# print(lst)

# import turtle
# screen = turtle.Screen()
# t = turtle.Turtle()
# hoizont = 200
# vert = 100
# t.color("turquoise", "green")
# t.pensize(10)
# t.speed(5)
#1-самая медленая
# 10 - очень быстро
#0 - самая бастрая
#
# t.begin_fill()
#
# t.forward(hoizont)
# t.right(90)
# t.fd(vert)
# t.right(90)
# t.forward(hoizont)
# t.right(90)
# t.fd(vert)
# t.right(90)
#
# t.end_fill()
#
# t.penup()
# t.goto(100, -30)
# t.pendown()
#
# t.fd(50)
# t.circle(50)
# t.color("blue")
# t.write("Movavi", font = ("Arial Black",50,"normal"),align="center")
#
# screen.exitonclick()    # выход при клике

# import random
# import time
# hacket = 0
#
# while hacket < 100:
#     hacket = hacket + random.randint(1,10)
#     if hacket >= 100:
#         print("Прогресс:",100,"%")
#     else:
#         print(f"Прогресс:{hacket}%")
#     time.sleep(2)

# import random
# variant = ["1️⃣","2️⃣","3️⃣"]
# guess = input("Где шарик?1️⃣,2️⃣,3️⃣")
# answer = random.choice(variant)
# if guess == answer:
#     print("🤗")
# else:
#     print("Не-а, он был в", answer)
#
# import turtle
# import random
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
#
# colors = ["red","blue","green","yellow","pink","purple"]
# side = 100
#
# i = int(input("Сколько углов?"))
# for j in range(0, i):
#     t.color(random.choice(colors))
#     t.color()
#     t.fd(side)
#     t.rt(360/i)
#
# screen.exitonclick()

import time
import random
print("Время пострелять...")
is_game = True
while is_game:
    patron = random.choice([1,2,3,4,5,6])
    our = random.choice([1,2,3,4,5,6])
    print("Заряжаем револьвер")
    time.sleep(1)
    print("Крутим барабан")
    time.sleep(2)
    print("Выстрел через")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("*Выстрел*")
    if patron == our:
        print("Смерть🤥")
        is_game = False
    else:
        print("Ты жив!")
        if (input("Играем снова?") == "нет"):
            is_game = False
        else:
            pass
pastebin.com/9ZmV5be9