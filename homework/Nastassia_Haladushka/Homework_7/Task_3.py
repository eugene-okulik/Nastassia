# Допустим, какая-то программа возвращает результат
# своей работы в таком виде:

# результат операции: 42

# результат операции: 54

# результат работы программы: 209

# результат: 2

# Нужно сделать всё то же самое, но уже способ -
# на ваше усмотрение (можно с помощью срезов и метода index,
# а можно с помощью split ). Получите из каждой строки
# с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.
# Главное отличие - выполните всё с использованием функций.
# Нужно сделать так, чтобы строк кода стало как можно меньше,
# и не было повторений одного и того же.

results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

total_sum = 0

for result in results:
    number = int(result.split(':')[-1].strip())
    total_sum += number + 10

print("Результат сложения:", total_sum)
