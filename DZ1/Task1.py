# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input())

c = n % 10
b = n // 10 % 10
a = n // 100

print ( a + b + c)