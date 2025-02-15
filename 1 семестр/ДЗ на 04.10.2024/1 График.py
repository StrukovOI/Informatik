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

#plt.scatter(x, y, c=y, cmap='flag', marker='o')
plt.plot(x, y, color='C1', marker='4', markersize=5)
plt.grid(True, which='major', axis='both', linestyle='dashdot')
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

plt.title('График радомных чисел')
plt.xlabel('Рандомные числа', alpha=0.5) 
plt.ylabel('Тоже рандомные числа', alpha=0.5) 

plt.show()