# *** Коллекции (контейнеры) ***

#  ** Список (list)

# Создание пустого списка
my_list = []
my_list = list()

# PEP8

# Добавить объекта (элемента) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("hello")
my_list.append([10, 20, 30])

# print(my_list)

# Чтение значений элемента
# Прямая индексация
# В квадратную скобачку указываем индекс
el = my_list[3]
el = my_list[3][1]

# Обратная индексация
el = my_list[-1]

# Замена значения элемента 
my_list[0] = 2000

# Удаление элемента по значению
# my_list.remove(3.14)

# Удаление элемента по индексу
del my_list[-1]


# Срез списка
s = "Hello, World!"
my_list = list(s)

# срез со 2-го индекса до конца исходного списка
my_slice = my_list[2:]

# срез со 2-го индекса до 5-го индекса не включительно
my_slice = my_list[2:5]

# срез с начала до 5-го индекса не включительно
my_slice = my_list[:5]

# срез со 2-го индекса до 12-го не включительно
# с шагом 2
my_slice = my_list[2:12:2]

# срез с применением обратной индексации
my_slice = my_list[-2:5:-1]

# переворот списка
my_slice = my_list[::-1]

# len() возвращает длину (кол-во элементов) коллекции
# print(len(my_list))
# print(my_list)
# print(my_slice)


# *** Кортеж (tuple) ***

# неизменяемая (immutable) коллекция
# легковеснее, чем список

# создание кортежа
my_tuple = (10, 20, 30, 40, 50)

# my_tuple[0] = 100

# print(my_tuple)

# # чтение значения элементов
# print(my_tuple[0])

# #  срез
# print(my_tuple[2:])


# *** Словарь (dict) ***

# изменяемый, упорядочинный тип коллекции

# пара "ключ-значения"
# {ключ_1:значение_1, ключ_2:значение_2}

# создание словаря
my_dict = {10:3.14, "abc":[1,2,3]}

# print(my_dict)

# чтение значений
# print(my_dict[10])
# print(my_dict["abc"])

data0 = {"name":"Aiyyskhan", "age":34, "id":123.5}
data1 = {"name":"John", "age":30, "id":12.5}
data2 = {"name":"Kate", "age":25, "id":3.0}

total_data = {"p0":data0, "p1":data1, "p2":data2}

# print(total_data["p1"]["name"])

# изменение значений
my_dict["abc"] = "hello"

# добавления новой пары 
# при присвоении нового значения по несуществующему ключю
# создается новая пара
my_dict['A'] = 777

# удаление пары (элементов)
del my_dict[10]

# обновление данных

data0 = {"name":"Aiyyskhan", "age":34, "id":123.5}

data0.update({"age":35, "id":300, "w":67.5})

# print(data0)


# *** Множество (set) ***

# изменяемый тип коллеуции

# Особенности:
# - неупорядоченный тип коллекции (объекты не игдексируются)
# - автоматом удаляет дублирующие объекты

# создание пустого множества
my_set = set()

# создание наполненного множества
my_set = {10, 20, 30}

# добавление элемента
my_set.add(123)

# когда добавляется значения,
# которое уже есть во множестве,
# то оно не добавляетс
my_set.add(30)

# удаления элемента
my_set.remove(20)
# my_set.remove(40)

# метод удаление без ошибок
my_set.discard(123)


# Дано два множества
w = {"a", "b", 'c', 'd'} 
z = {'b', 'c', 'q'}

# объединение
f = w.union(z)
f = w | z

# пересечение
f = w.intersection(z)
f = w & z

# разность
f = w.difference(z)
f = z.difference(w)
f = w.symmetric_difference(z)
# короткая запись difference
f = w - z

# самостоятельно поэксперементировать с оставшимися методами
# рассмотреть модуль collections

print(f)