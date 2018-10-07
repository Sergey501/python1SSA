import math

# coding: utf-8
__author__ = 'Семьянинов Сергей Андреевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = max(list(input("Введите число")))
print(x)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input("Введите число А: ")
b = input("Введите число Б: ")

a, b = b, a

print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = int(input("Введите коэфициент а: "))
if a <= 0:
   print("Значение должно быть больше или равно 1")
else:
   print("Теперь введите коэфициент b")
b = int(input("b: "))
if b <= 0:
   print("Значение должно быть больше или равно 1")
else:
   print("Теперь введите коэфициент c")
c = int(input("c: "))
if c == 0:
   print("Значение c не должно быть равно 0")
else:
   print("Приступаем к решению уравнения")
# a * (x ** 2) + b * x + c
diskr = ((b ** 2) - (4 * (a * c)))
if diskr < 0:
    print("Решений нет")
elif diskr == 0:
    x = (-b)/(2*a)
    print(x)
else:
    x_1 = ((- b) + (math.sqrt(diskr)))
    x_2 = ((- b) - (math.sqrt(diskr)))
print(x_1)
print(x_2)
