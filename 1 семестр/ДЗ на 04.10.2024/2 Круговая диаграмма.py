import numpy as np
import matplotlib.pyplot as plt
ax=plt.gca()
import matplotlib.ticker as ticker
import random

x=[]
for i in range(5):
    x.append(random.uniform(0, 20))

plt.pie(x, labels = [x[3], x[2], x[0], x[1], x[4]], autopct='%1.g%%')
plt.title('Рандомная диаграмма')

plt.show()