# x = 7
# if x <= 7:
#     print("Меньше или равно")
# else:
#     print("Больше")

# x = 7
# if (x == 7 or x < 7) and x <= 7:
#     print("Ура")
# print(x == 7)
#
# x = int(input("Вевди число:)"))
# if x < 0:
#     print("отрицательное")
# elif x > 0:
#     print("положительное")
# else:
#     print("ноль")

# year = int(input("Вевди год:)"))
# if year % 4 == 0 and (year % 400 == 0 or year % 100):
#     print("Висосокосненько")
# else:
#     print("Не високосненько")
#
# number1 = int(input("Ввевди число:"))
# operation = input("Вевди операцию:")
# number2 = int(input("Ввевди число:"))
#
# lst = ["+","-","/","*"] # список возможных операций
# if operation in lst: #если операция возможна
#     if operation == "+":
#         print(number1 + number2)
#     elif operation == "-":
#         print(number1 - number2)
#     elif operation == "/":
#         print(number1 / number2)
#     elif operation == "*":
#         print(number1 * number2)
# else:
#     print("Написал фигню")
#
# number1 = int(input("Введи число:"))
# number2 = int(input("Введи число:"))
# number3 = int(input("Введи число:"))
# count_pol = 0
# count_otr = 0
#
# if number1 > 0:
#     count_pol += 1
# elif number1 < 0:
#     count_otr += 1
#
# if number2 > 0:
#     count_pol += 1
# elif number2 < 0:
#     count_otr += 1
#
# if number3 > 0:
#     count_pol += 1
# elif number3 < 0:
#     count_otr += 1
#
# print("Положительных:", count_pol)
# print("Отрицательных:", count_otr)

# number1 = int(input("Введи число:"))
# number2 = int(input("Введи число:"))
# number3 = int(input("Введи число:"))
# lst = [number3,number2,number1]
# maxi = max(lst)
# # mini = min(lst)
# print("самое маленькое",mini)
# print("самое большое",maxi)
#
# h =int(input("Введи число:"))
# m =int(input("Введи число:"))
# s =int(input("Введи число:"))
# if (h > 23 or h < 0) or  (m > 59 or m < 0) or  (s > 59 or s < 0):
#     print("фигня полная:(")
# else:
#     print("формат верный:)")
#     print(f"{h}:{m}:{s}")
#
# ticket = input("Введите число(6 цифр)")
# if len(ticket) == 6 and ticket.isdigit():  # число ли это
#     f_half = ticket[:3]
#     l_half = ticket[-3:]
#     f_sum = int(f_half[0])+int(f_half[1])+int(f_half[2])
#     l_sum = int(l_half[0]) + int(l_half[1]) + int(l_half[2])
#     if f_sum == l_sum:
#         print("билет счастливый:)")
#     else:
#         print("не повезло:(")
# else:
#     print("Ну ты чет фигню вписал")
#
# month = input("номер месяца").strip()
# if month.isdigit() and 12 >= int(month) >= 1:
#     month = int(month)
#     if 3 >= month >= 5:
#         print("Весна")
#     elif 6 >= month >= 8:
#         print("Лето")
#     elif 9 >= month >= 11:
#         print("Осень")
#     else:
#         print("Зима")

hamsters = int(input("Количество хомяков"))
if 11 <= hamsters <= 19:
    print(hamsters, "хомяков")
elif hamsters % 10 == 1:
    print(hamsters, "хомяк")
elif 2 <= hamsters % 10 <= 4:
    print(hamsters, "хомяка")
else:
    print(hamsters, "хомяков")
