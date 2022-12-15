# nums = [1, 2, 3, "Hello world", True, 3.5, [1, 2]]
# print(nums)
# print(nums[3])
# print(nums[:3])

# num = []
# num.append(123)
# num.append("hello")
# print(num)

# nums = []
#
# for i in range(101):
#     nums.append(i)
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         print(nums[i])
# nums = []
# for num in nums:
#     print(num)

# array = ["dogs","cats","rabbits"]
# array[0] = "fish"
# print(array)

# nums = []

# for i in range(len(nums)):
#     if i % 2 == 0:
#         nums[i] = "even"

#task 1

# nums = []
# a = int(input("Введи число а"))
# b = int(input("Введи число b"))
#
# for i in range(a+1, b):
#     nums.append(i ** 2)
#
# print(nums)
#
# array = [123, True, "text", [1,2]]
# array.reverse()
# print(array)

#task 3
# nums = []
# while True:
#     num = input("Введите число:")
#     if not(num.isdigit()):
#         break
#     else:
#         nums.append(int(num))
# print(nums)
#
# even = 0
# odd = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Четных:", even, "Нечетных:", odd)

#task 4
# nums = [2,4,5,3,7,6,9,8,10]
# enter = []
# for i in range(1, len(nums)):
#     if nums[i] > nums[i-1]:
#         print(i)

#task 5
# nums = [2,4,5,3,7,6,9,8,10]
# a = min(nums)
# b = max(nums)
# a_ind = nums.index(a)
# b_ind = nums.index(b)
#
# nums.insert(a_ind, b)
# nums.pop(a_ind  + 1)
# nums.insert(b_ind, a)
# nums.pop(b_ind+1)
# print(nums)

#task 6
#
# nums_str = input("enter numbers")   #1 2 3 4 5
# nums_list = nums_str.split(" ")
# white_list = []
# for num in nums_list:
#     if num not in white_list:
#         white_list.append(num)
# print(nums_list)
# print(len(white_list))

#tasks in codewars

from random import randint

nums =[]
решить 7 и 8 задачи