"1"
def decor(func):
    def decor2(*args):
        result = func(*args)
        print(f"Вызвана функция {func}.Результат:{result}, аргументы:{args}")
        return result
    return decor2

@decor
def f(a, b):
    return a * b
f(5, 10)







"2-3"
def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper
@validate_args
def argument(x):
    return x

print(argument(1))
print(argument())
print(argument(1, 2))
print(argument(0.5))
print(argument(-1))




"4"
def decor(func):
    def wrapper(*args):
        print("Подтверждаете выполнение функции?(Да/Нет)")
        accept = input()
        if accept == "Да":
            return func(*args)
        elif accept == "Нет":
            return
        else:
            print("Данные некорректны")
            return wrapper(*args)
    return wrapper

@decor
def f(a, b):
    return a * b
print(f(5, 10))




"5"

import time
def time_func(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        res = (t2 - t1) / 1000
        print(f"Время работы {res}")
        return res
    return wrapper

@time_func
def time1():
    a = [i for i in range(1, 1000000)]
    return a
time1()

