# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число n: '))
sum = 0
num_list = []

for i in range(1, n+1):             
    num = (1 + 1 / i) ** i
    sum += num
    num_list.append(sum)
print(sum)