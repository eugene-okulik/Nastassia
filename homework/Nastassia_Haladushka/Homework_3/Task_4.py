# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
from math import sqrt
a = 3
b = 4
c = sqrt((a ** 2) + b ** 2)
s = (a * b) / 2
print("Гипотенуза прямоугольного треугольника составляет:", c)
print("Площадь прямоугольного треугольника составляет:", s)
