# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10, результат сложения распечатайте.

text_one = 'результат операции: 42'
text_two = 'результат операции: 514'
text_three = 'результат работы программы: 9'

print(int(text_one[text_one.index(':') + 2:]) + 10)
print(int(text_two[text_two.index(':') + 2:]) + 10)
print(int(text_three[text_three.index(':') + 2:]) + 10)
