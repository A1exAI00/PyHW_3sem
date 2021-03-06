'''
Найти в интернете функции, вычисляющие число PI до n десятичных знаков. (n ~ 100000 - 10^6)
Построить гистограмму частоты появления цифр в числе PI
Построить гистограмму частоты появления двукзначных чисел в числе PI
'''

import sympy
import matplotlib.pyplot as plt

# Рассчет Пи
pi = sympy.pi.evalf(100)
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