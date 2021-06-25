# *** Генератор паролей ***

import hashlib
from tkinter import StringVar, Tk, Label, Entry, Button
from typing import Text

def hashing(pwd):
    """
    функция хеширования

    :Принимает строку пароли и "соль"
    :Возвращает хеш-строку
    """

    # прием строки человекочитаемой пароли с "солью"
    pwd = pwd.get()
    # кодирование в байт-строку
    byte_str = pwd.encode()
    # хеширование (применение хеш-функции из модуля hashlib)
    hash_str = hashlib.sha256(byte_str)
    # преобразования хеш-строки спец типа в обычную строку типа str
    hex_str = hash_str.hexdigest()[:10]
    # переача захешированной строки
    hash_pwd.set(hex_str)

    # print(hex_str)
    # print(type(hex_str))

# hashing("qwerty")

# объект окна
window = Tk()
window.title("Password generator v.0.1")



# переменные класса StringVar
pdw = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0, padx=5, pady=5)
# виджет поля ввода
Entry(textvariable=pdw).grid(row=0, column=1, padx=5, pady=5)
# виджет кнопки
Button(text="СТАРТ", command=hashing).grid(row=1, column=0, padx=5, pady=5)
# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=5, pady=5)

# запуск программы (точка входа программы)
window.mainloop()

# модуль pyinstaller
# pip install pyinstaller - команда установки модулей