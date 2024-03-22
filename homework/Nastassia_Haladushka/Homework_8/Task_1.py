# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.

# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])

if bonus is True:
    salary_with_bonus = salary + random.randint(1, 100000)
    print(f"{salary}, {bonus} - '${salary_with_bonus}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
