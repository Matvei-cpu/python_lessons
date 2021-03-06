# *** Функции ***

# встроенная функция ввода данных
# data = input("Введите данные: ")

# print(f"Вы ввели вот это - {data}")

# Создание (определение) Функции

# 1 вариант. Функция, принимающая данные (обладающая аргументами)
def func_1(arg_1):
    s = arg_1 ** 2
    w = s + 10
    print(f"Результат: {w}")

# Вызов функции
# func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res += 200
    print(res)

# func_2(10, 5, 2)

# аргумент может иметь значения по умолчанию
def func_3(arg_1, arg_2=100):
    print(arg_1 * arg_2)

# func_3(20, 10)
# func_3(100)
# func_3(3.14)

# 2 вариант юфункция возвращающая данные
def func_4(arg_1, arg_2):
    res = arg_1 + arg_2
    return res

# d = func_4(10, 10)

def func_5(x, y):
    res_1 = x * y
    res_2 = x * y
    return res_1, res_2, x

# первый способ приема данных
d_1 = func_5(10, 2)
#второй способ приема данных 
a, b, c = func_5(10, 2)

# print(d_1)
# print(d_1[0])

# print(a, b ,c)
# print(b)


# *** Безымянные функции (лямбда-выражения, лямбда-функции)

# Особенности:
# - всегда обладают аргументами
# - всегда возвращает результат

# Пример 1. Лямбда внутри гениратора списка
my_list = [(lambda arg_1: arg_1.upper())(i) for i in "hello"]

# Пример 2. Словарь лямбда-выражений
my_lambdas = {
    "*": lambda arg_1, arg_2: arg_1 * arg_2, 
    "+": lambda w, z: w +z
}

# print(my_lambdas["+"](5,2))
# print(my_lambdas["*"](5,2))


# *** декоратор ***

# Декоратор - функции, обертывающая другую (таргетную) функцию.

# декоратор
def my_decorator(func_object):
    # функция-обертка
    def wrapper(w):
        # доп функциональность ДО
        print("Before")
        w = w + 2
        # вызов целевой функции
        func_object(w)
        # доп фунциональность ПОСЛЕ
        print("After")
    # возврат объекта функции-обертки
    return wrapper

# новый способ применения декоратора
@my_decorator
# Целевая (таргетная) функция
def target_func(arg_1):
    print("Hallo! I am target func :)", arg_1)

# старый способ применения декоратора
# target_func = my_decorator(target_func)

target_func(10)