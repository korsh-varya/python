# a = int(input("веди число а"))
# b = int(input("веди число b"))
# print(a)
# while a < b:
#     a = a + 1    #a += 1  так тоже можно
#     print(a)

#минимальное количество строчек для того чтобы сделать последовательность в while
# a = 0
# while a < 10:
#     a = a + 1    #a += 1  так тоже можно
#     print(a)

#for параметр in последовательность:
#   действия...

#минимальное количество строчек для того чтобы сделать последовательность в for
# for i in range(2, 10 + 1):         #range - последовательность(только с целыми)
#     print(i)                    #последнее число не включает

# a = int(input("веди число а"))
# b = int(input("веди число b"))
# for i in range(a,b):
#     print(i)

# steps = int(input("Сколбко ярусов"))
# for i in range(1, steps + 1):
#     print("#"*i)

# steps = int(input("Сколько ярусов"))
# sim = input("Какой символ?")
# for i in range(1, steps + 1):
#     print(" " * (steps - i) + sim * i + sim * i)

# steps = int(input("Сколько ярусов"))
# sim = input("Какой символ?")
# sim1 = input("Какой символ?")
# print(" " * (steps - 1) + '⭐')
# for i in range(1, steps + 1):
#     if i % 2 == 0:
#         print(" " * (steps - i) + sim * i + sim * i)
#     else:
#         print(" " * (steps - i) + sim1 * i + sim1 * i)
# print(" "* (steps-2),"||")


#cамостоятельные задачи
# num = int(input("Введите число:"))
#
# for i in range(1,10+1):
#     print(f"{num} * {i} = {num * i}")

# v = int(input("Введите высоту"))
# g = int(input("Введите длину"))
#
# for i in range(1,v + 1):
#     print(" # " * g)

# for i in range(1 , 50 + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz⚡")
#     else:
#         print(i)

v = int(input("Введите высоту"))
g = int(input("Введите длину"))

print(v * "#")
for i in range(2, v):
    print("#", " ")     #дорешать!!!