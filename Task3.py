# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = lambda a, b: a**2 == b or b**2 == a
print(x(a,b))