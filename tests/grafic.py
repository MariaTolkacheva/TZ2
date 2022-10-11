import matplotlib.pyplot as plt
import numpy as np
import random
import time
from functions import *
time_data=[]
set = []
k=0
for i in range(1,1000):
    set+= [i]
    start_time = time.time()
    num_min(set)
    num_prod(set)
    num_sum(set)
    num_max(set)
    end_time = time.time()
    time_data.append((end_time-start_time)*100)
print(time_data)
ypoints = np.array(time_data)
xpoints = np.array([i for i in range(len(time_data))])

plt.plot(xpoints, ypoints)
plt.show()




x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(3 * x) / x
plt.plot(x, y)
plt.show()

import pandas as pd

data = {'series2': [2, 4, 5, 2, 4],
        'series3': [3, 2, 3, 1, 3]}
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([0, 5, 0, 7])
plt.plot(x, df)
plt.legend(data, loc=2)
plt.show()
