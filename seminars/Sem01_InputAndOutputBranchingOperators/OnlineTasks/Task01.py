"""Задача No1:
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

Например:
Input:
-   n = 700
-   m = 750
Output:
-   2
"""
n = int(input('Сколько машина проедет за день: '))
m = int(input('Какой путь нужно проехать: '))

result = (n + m - 1) // n

print('Понадобиться', result, 'дней')