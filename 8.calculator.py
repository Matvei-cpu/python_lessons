# *** Пример. Калькулятор ***

# функция-обработчик
def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        pesult = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif:
        result = (f"Что это такое {op}? :(")


# цикл программы
while True:
    # ввод данных
    cmd = input("Командуйте, сэр :) ")
    if cmd == "stop":
        print("Buy buy!")
        break

    nam_1 = int(input("Введите 1 число: "))
    nam_2 = int(input("Введите 2 число: "))
    op = input("Введите символ операции: ")

    # обработка данных
    result = calculate(num_1, nam_2, op)

    # вывод данных
    print(f"Результат: {result}")