import random
import re

# easy
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# создаем произвольный список:
x = [random.randint(-10, 10) for _ in range(10)]
print("произвольный список = ", x)
# определяем функцию с генератором для возведения элементов списка в квадрат
def quadro (x):
    for i in x:
        if i == i:
            yield i**2
# выводим значение
print(list(quadro(x)))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruilist1 = {"apple", "orange", "grape", "watermelon", "peach"}
fruilist2 = {"apple", "banana", "kiwi", "grape", " cherry"}

print(list(fruilist1 & fruilist2))
# альтернативное решение

fruilist1 = ["apple", "orange", "grape", "watermelon", "peach"]
fruilist2 = ["apple", "banana", "kiwi", "grape", " cherry"]

dublikat_list = [fruit for fruit in fruilist1 if fruit in fruilist2]
print(dublikat_list)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lsty = [random.randint(-10, 10) for _ in range(10)]
print("произвольный список = ", lsty)

lsty = [el for el in lsty if (el % 3 == 0 and el > 0 and el % 4 != 0)]

print(lsty)

# normal

# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
# рещение без функции re
def without_re2(line):

    result_list = list()
    for index in range(2, len(line) - 2):
        if line[index].isupper() and line[index - 2: index].islower() and line[index + 1: index + 3].isupper():
            if index > 2 and index < len(line)-3:
                if line[index - 3].isupper() and line[index + 3].islower():
                    result_list.append(line[index])
            else:
                result_list.append(line[index])
    return result_list
# решение с использование функции re
def with_re2(line):
    result_list = list()
    patern = '(?=([A-Z]{1}[a-z]{2}[A-Z]{3}[a-z]{1}))'
    result = re.findall(patern, line)
    print(result)
    for string in result:
        result_list.append(re.findall('[A-Z]', string)[1])
    return result_list
print(with_re2(line_2))
print(without_re2(line_2))

# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле

with open('fileL1L4.txt', 'w') as my_file:
    for _ in range(2500):
        my_file.write(str(random.randint(0, 9)))
with open('fileL1L4.txt', 'r') as my_file:
    longest_sequences = list()
    numbb = my_file.read()
    print(numbb)
    for number in range(0, 10):
        if str(number) in numbb:
            lst = re.findall('[%s]+' % number, numbb)
            longest_sequences.append(max(lst, key=len))
    result = max(longest_sequences, key=len)
    print(result)
#HARD

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2],]

# Выполнить поворот(транспонирование) матрицы
# Пример Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

#print(np.matrix(matrix).transpose())
matrix_rotate = [list(el) for el in zip(*matrix)]
print(matrix_rotate)