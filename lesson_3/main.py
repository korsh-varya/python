# x =input("введите что нибудить:")
# temp = x[-1]
# print(x.index(temp)+1)
# print(len(x))

# name1 = "Anton"
# name2 = "Vova"
# name3 = "Bogdan"
# bratva = [name1,name2,name3]
# print(bratva)
# # print(bratva[0][2:])    #bratva[0] - Антон,2[2:] - срез Антона
#
# path = "C:/Python3/python.exe"
# print("Имя файла:",path[11:])
# print("Расширение:",path[-3:])
# print("Имя католога:",path[3:10])
# print("Полный путь к катологу",path[:10]) #можно пустоту вместо нуля или пустоту вместо последней цифры

# path = "C:/Python3/python.exe"
# temp = path.split("/")
# print(temp)
# print("Имя файла:",temp[-1])
# print("Расширение:",temp[-1][-3:])
# print("Имя католога:",temp[1])
# print("Полный путь к катологу",temp[0]+"/"+temp[1])

# chapter1 = input("Глава:")
# page1 = input("страница:")
#
# chapter2 = input("Глава:")
# page2 = input("страница:")
#
# chapter3 = input("Глава:")
# page3 = input("страница:")
# print(chapter1.ljust(15),page1.rjust(15))
# print(chapter2.ljust(15),page2.rjust(15))
# print(chapter3.ljust(15),page3.rjust(15))

# x = "123456789"
# print(x[::2])       #через один
# print(x[::-1])       #в обратном порядке
# print(x[::-2])      #в обратном порядке через один

x = "12'345'678"
# temp = x[:2] + x[3:5] + x[-3:]
# number = int(temp)
# print(temp)
# #решение черз срезы

# temp = x.split("'")
# temp2 = temp[0] + temp[1] + temp[2]
# number = int(temp2)
# print(number)

# temp = x.replace("'","")
# number = int(temp)
# print(number)