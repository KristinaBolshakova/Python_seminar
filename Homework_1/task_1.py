# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input('Введите цифру, обозначающую день недели: '))
if num == 6 or num == 7:
    print('Да, этот день является выходным!')
elif 1 <= num <= 5:
    print('Нет, этот день не является выходным!')
else:
    print('Такого дня недели нет')