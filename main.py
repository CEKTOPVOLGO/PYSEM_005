# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
'''

def stepen(a: int, b: int, result: int):
    if b == 0: 
        print (result)
    else:
        stepen(a, b - 1, result * a)      


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = 1
stepen(a, b, result)
'''


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def summ(a: int, b: int):
    if b == 0:
        print(a)
    else:
        summ(a + 1, b - 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

summ(a, b)