# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка
# пятое число, двухсотое число, тысячное число, стотысячное число

def fibonacci_generator():
    a, b = 0, 1
    count = 0

    while True:
        yield a
        a, b = b, a + b
        count += 1


fib_gen = fibonacci_generator()

for i in range(1, 100001):
    current_number = next(fib_gen)

    if i == 5:
        five = current_number
    elif i == 200:
        two_hundred = current_number
    elif i == 1000:
        thousand = current_number
    elif i == 100000:
        hundred_thousand = current_number

print("Пятое число Фибоначчи:", five)
print("Двухсотое число Фибоначчи:", two_hundred)
print("Тысячное число Фибоначчи:", thousand)
print("Сто тысячное число Фибоначчи:", hundred_thousand)
