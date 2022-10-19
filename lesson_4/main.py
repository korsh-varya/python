# #урок 4
# a = input("фамилия").capitalize()
# b = input("имя").capitalize()
# c = input("отчество").capitalize()
# # 2 варианта одинаковова вывода
# print(a,b[0]+".",c[0]+".")
# print(f"{a} {b[0]}.{c[0]}.")
# #.capitalize() -
#
# x = "abracadabra"
# print(x.count("a"))
# #count() - подсчет

# x = "Hello, world"
# lst = x.split(" ")
# lst.remove("world") # по значению
# lst.pop(0) #по индексу

# fraze = input("vvedite clovo")
# find = input("что меняем")
# Replace = input("на что меняем")
# fraze.replace(find,replace)

# x  = input()
# print(x.replace("йо","ё"))

# abc = {"а":"a",
#        "б":"b",
#        "в":"v",
#        "г":"g",
#        "д":"d",
#        "е":"e",
#        "ё":"yo",
#        "ж":"zh",
#        "з":"z",
#        "и":"i",
#        "к":"k",
#        "л":"l",
#        "м":"m",
#        "н":"n",
#        "о":"o",
#        "п":"p",
#        "р":"r",
#        " ":" ",
#        }
# x = input("Введите фразу:").lower()
# translate = ""
# for bukva in x:
#     translate = translate + abc[bukva]
# print(translate)

# x = input("Введите логин:")
# temp = x.split("@")
# print("Логин:",temp[0],"Домен:",temp[1])

#урок 5
# x = 5
# if x == 5:
    # print("Ура")
# if x < 10 and x > 6:
    # print("Ура")
# if x < 10 or x > 6:
    # print("Ура")
# while True:
    # print("приветики")
# x = int(input("Введите число"))
# if x<0:
#     print("отрицательное число")
# elif x > 0:
#     print("положительное число")
# else:
#     print("нуль")

year = int(input("Год:"))
if year % 4 == 0 and (year % 400 == 0 or year % 100):
    print("Год високосный")
else:
    print("Год не високосный")