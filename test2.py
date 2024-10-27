# def cache_deco(func):
#     cache = {}
#
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#
#     return wrapper
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
# import time


# def repeat_deco(n=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)


# a = int(input())
# def f():
#     global a
#     a += 10
# f()
# print(a)


# def g():
#    b = int(input())
#    def h():
#        nonlocal b
#        b += 10
#    h()
#    print(b)
# g()



# from typing import List, Dict
#
# def make_most_common_keys(d: Dict[int, int]) -> List[int]:
#
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)



# def f(listt):
#     listt2 = []
#     for i in range(0, len(listt), 2):
#         listt2.append(listt[i] ** 0.5)
#     return listt2
#
# print(f(list(map(int, input().split()))))


# def f(st):
#     st = st.upper()
#     st = st[::-1]
#     return st
# print(f(input()))


# def f(st):
#     b = []
#     a = "0123456789"
#     for i in range(len(st)):
#         if st[i] in a:
#             b.append(st[i])
#     return set(b)
# print(f(input()))



# def f(st):
#     st1 = ""
#     for i in range(len(st)):
#         if st.count(st[i]) == 1:
#             st1 += st[i]
#     return st1 + "япидорас"
#
# print(f(input()))





# from typing import List, Dict
#
# def make_most_common_keys(d: Dict[int, int]) -> List[int]:
#     sortkey = sorted(d.keys(), key=lambda k: d[k], reverse=True)
#     return sortkey
#
#
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)





# from typing import List
#
# def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
#     return [i for i, (num1, num2) in enumerate(zip(nums1, nums2)) if num1 < num2]
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)


# def f(list):
#     a = []
#     for i in list:
#         if i ** 0.5 == int(i ** 0.5):
#             a.append(i)
#     return a


# def f(st):
#     a = ""
#     j = 0
#     for word in st.split():
#         j = max(len(word),j)
#         if j == len(word):
#             a = word
#     b = ""
#     g = 0
#     for word in st.split():
#         g = max(st.count(word), g)
#         if g == st.count(word):
#             b = word
#     return a, b
#
#
# print(f("a bb ccc dddd ddd bb ccc bb"))


# def f(number):
#     count = 0
#     for i in str(number):
#         count += int(i)
#     return count
#
# print(f(1234))


# def cache_deco(func):
#     cache = {}
#
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#
#     return wrapper
#
#
# def solution(func_map, func_filter, data):
#     filtered_data = (func_map(item) for item in data if func_filter(item))
#     for index, item in enumerate(filtered_data):
#         if index % 2 == 0:
#             yield item
#
#
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)


# class Counter:
#
#     def __init__(self, initial_count):
#         self.initial_count = initial_count
#
#     def increment(self):
#         self.initial_count += 1
#
#     def get(self):
#         return self.initial_count
#
#
# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
#
#
# class Circle:
#    pi = 3.14
#
#    def calculate_area(self, radius):
#       return self.pi * radius ** 2
#
#
# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)


# def decor(func):
#     def decor2(*args):
#         result = func(*args)
#         print(f"Вызвана функция {func}.Результат:{result}, аргументы:{args}")
#         return result
#     return decor2
#
# @decor
# def f(a, b):
#     return a * b
# f(5, 10)
#
#
#
#
# import time
#
# def time_func(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         res = (t2 - t1) / 1000
#         print(f"Время работы {res}")
#         return res
#     return wrapper
#
# @time_func
# def time1():
#     a = [i for i in range(1, 1000000)]
#     return a
# time1()



# def validate_args(func):
#     def wrapper(*args):
#         if len(args) < 1:
#             return "Not enough arguments"
#         elif len(args) > 1:
#             return "Too many arguments"
#         elif not isinstance(args[0], int):
#             return "Wrong types"
#         elif args[0] < 0:
#             return "Negative argument"
#         return func(*args)
#     return wrapper
# @validate_args
# def argument(x):
#     return x
#
# print(argument(1))
# print(argument())
# print(argument(1, 2))
# print(argument(0.5))
# print(argument(-1))
#
#
# def decor(func):
#     def wrapper(*args):
#         print("Подтверждаете выполнение функции?(Да/Нет)")
#         accept = input()
#         if accept == "Да":
#             return func(*args)
#         elif accept == "Нет":
#             return
#         else:
#             print("Данные некорректны")
#             return wrapper(*args)
#     return wrapper
#
# @decor
# def f(a, b):
#     return a * b
# print(f(5, 10))


class Zoo:
    def animal(self, an):
        self.an = an

    def voice(self, value, name):
        print(f'Животное {name} издает звук {value}')

cat = Zoo()
dog = Zoo()
cat.voice('Мяу', 'Кошка')
dog.voice('Гав', 'Псина ебаная')







