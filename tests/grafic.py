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
    time_data.append((end_time-start_time)*1000)
print(time_data)
ypoints = np.array(time_data)
xpoints = np.array([i for i in range(len(time_data))])

plt.plot(xpoints, ypoints,'o')
plt.xlabel("количество цифр")
plt.ylabel("Примерное время выполнения")
plt.show()
