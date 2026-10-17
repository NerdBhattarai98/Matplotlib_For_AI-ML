import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020,2021,2022,2023,2024,2025])
y = np.array([15,25,30,44,33,22])

plt.plot(x,y) #If only one argument passed this will be on z axis and put each increment on 1 (0 ma 15 25 ma 1 types)

plt.show()