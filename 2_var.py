# однострочный коммент
# "ctrl+/"
# print("hello world")
# print("hell")
# print("thailand")

'''какой то 
многострочный 
коммент'''

"""i am
a 
millionnair"""

# переменные

# var_1 = 100
# print(var_1)
# snake_case
# number_of_apples = 10
# camelCase
# numberOfBananas = 20

# константы
# CONST_VAR = 1000

# вызов встроенной функции вывода в терминал
# print(numberOfBananas, CONST_VAR)

# встроенная функция ввода из терминала
# my_input = input("Введите что-то: ")

# print("Вы ввели вот это -". my_input)

# небольшой калькулятор

# num_1 = input("введите 1 число: ")
# num_2 = input("введите 2 число: ")

# конкатенация строк
# int
# result = num_1 + num_2 

# конвертация данных
# result = int(num_1) + int(num_2)

# print("Результат =", result)
# print("hello world")
# int
# num_1 = input("число1")
# num_2 = input("число2")
# result =2*int(num_1) + int(num_2)
# print("результат =",result)
# print(int(input("первое число: ")) + 2*int(input("второе число: ")))
S = input("Напишите сумму кредита: ")
N = input("Напишите срок кредита: ")
P = input("Ставка кредита:  ")
I = int(P) / 1200
C = int(S) * float(I) * (1 + float(I)) ** int(N) / ((1 + float(I)) ** int(N) - 1)
print("Ежемесячная оплата: ", C)


print(C)



