import numpy as np
import matplotlib.pyplot as plt
ax=plt.gca()
import matplotlib.ticker as ticker
import random

x=[]
y=[]
for i in range(100):
    x.append(random.randint(0, 100))
    y.append(random.randint(0, 100))

plt.bar(x, y, label='Случайное распределение случайных чисел по случайным числам', alpha=0.7)
plt.plot(x, y, color='C2', marker='^', markersize=4)
plt.legend(loc='best')

plt.show()