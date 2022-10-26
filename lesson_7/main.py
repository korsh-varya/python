# ZeroDivisionError
#x = 7/0

#TypeError
#x = 15+"a"

#NameError
# lst =[0,-5.5,"five"]
# print(x[3])

#SyntaxError
#x = "Hello, I am Varya

#ValueError
#int("a")

#NameError
#print(x)

#assert
# def summa(numbers):
#     return sum(numbers)
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4
#
# try:
#     div = int(input("Введи число, для деления:"))
#     x = 5/div
# except ZeroDivisionError:             # обработка деления на ноль
#     print("Ошибка деления на ноль")
# # except Exception:             # любая ошибка обработка
# #     print("Ошибка")
# except ValueError:
#     print("Введи циферку пожалуйста")
# else:               # ошибок не было
#     print("все good")
# finally:
#     print("Я проверил и попытался!")
# print("Я сработал")
#
# lst = []
# try:
#     f = open("file.txt")  # файл помещен в f
# except FileNotFoundError:
#     print("А файла то нет:(")
# else:
#     try:
#         for line in f:  # для каждой строчке в файле
#             lst.append(int(line))  # добавить список число
#     except ValueError:
#         print("Я хочу только цифры:(")
#     else:
#         print("Все хорошо")
#     finally:
#         f.close()
#print(lst)
#
# try:
#     x = 5/0
# except ZeroDivisionError as error_message:
#     print("Слушай а вот тут ошибочка возникла",error_message)
#
# x = input("Введи любое имя:").lower().strip()
# try:
#     if x == "антон":
#         raise Exception("Имя препода запрещено")
#         # raise - вызвать ошибку
# except Exception:
#     print("Я люблю Movavi, и препода в обиду не дам")