'''
Найти в Интернете функции, вычисляющие число sqrt(2) до n десятичных знаков (n ~ 100000 - 10^6)
Построить гистограмиу частоты появления цифр в числе sqrt(2)
Построить гистограмму частоты появления двухзначных чисел в числе sqrt(2)
'''

import sympy
import matplotlib.pyplot as plt

# Рассчет корня(2)
pi = sympy.sqrt(2).evalf(1000)
print(pi)

# Список с отдельными цифрами
dig = [str(pi)[i] for i in range(len(str(pi)))]

# Список с количеством каждой цифры
freq = [dig.count(str(i)) for i in range(10)]
print(freq)

# Создание гистаграммы
plt.bar(list(range(10)), height=freq)
plt.grid()
plt.show()

# Вторая часть вопроса (про появление двухзначных чисел)
# вообще не понятно что он имел в виду