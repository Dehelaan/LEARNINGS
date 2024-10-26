print('Working with Live data')

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



plt.style.use('fivethirtyeight')

x_vals=[]
y_vals=[]

index = count()

def animate(i):
#    x_vals.append(next(index))
#    y_vals.append(random.randint(0, 5))
#
#    plt.cla()
#    plt.plot(x_vals, y_vals)

    data = pd.read_csv('matplotlib_learning\live_data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label='channel A')
    plt.plot(x, y2, label='channel B')

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate,interval=1000)

plt.tight_layout()
plt.show()


