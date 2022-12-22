# nums = set()
# nums.add(1)
# nums.add(1)
# nums.add(2)
# print(nums)

# person = {
#     "name":"Ilya",
#     "age": "22",
#     "hobbies":["play guitar","read books"],
#     1:"math",
#     2:"python",
#     3:"JS"
# }
# print(person["name"])
# from random import randint
# nums = [randint(-100,100) for i in range(100)]
# a = list(set(nums))
# b = len(nums) - len(a)
# c = len(a) - b
# print(b)
# print(c)

# from random import randint
# n,m = int(int(input("N: "))),int(input("M: "))
# a = set([randint(0,1000) for i in range(n)])
# b = set([randint(0,1000) for i in range(m)])
#
# res1 =list(a & b)              # & бозначает пересечение
# res1.sort()
# print(len(res1))
# print(res1)
# print("_"*10)
#
# res2 =list(a - b)
# res2.sort()
# print(len(res2))
# print(res2)
# print("_"*10)
#
# res3 =list(b - a)
# res3.sort()
# print(len(res2))
# print(res2)
# print("_"*10)

#task 1
# from random import randint
# a = set([randint(0,10000) for i in range(10000)])
# b = set([randint(0,10000) for i in range(10000)])
# res = list(a|b)
# res.sort()
# print(res)

# task 2
# from random import randint
# a = [randint(0,10000) for i in range(10)]           # доделать!!!!!!!!!!!!!!
# n = []
# for i in range(len(a)):
#     if a[i] >= a[i-1]:
#         n.append(a[i])
#     else:
#         None
# print(n)

# task 3
# from random import randint
# num = str(randint(1,int(input("Enter number"))))
# right_quest = []
# while True:
#     quest = input("Биатриса какое это число").split(" ")                  # доделать!!!!!!!!!!!!!!
#     print("Игра Белатриса и Август")
#     if "help" in quest:
#         variants = right_quest[0]
#         for i in right_quest:
#             variants &= variants
#         print("Возможнае варианты:",variants)
#         quest = int(input("Итоговый ответ"))
#         if num in quest:
#             print("Да вы выиграли!🤣")
#         else:
#             print("Близко ,но не то...")
#     if num in quest:
#         print("Yes")
#         right_quest.append(set(quest))
#     else:
#         print("No")
# print("Игра окончена")

# text = input(" something").split()
# # \n
# for i in range(len(text)):
#     text[i] = text[i].strip("\\n")
# print("Different words",len(set(text))