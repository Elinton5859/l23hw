import numpy as np
import matplotlib.pyplot as plt
#initializing the sinwave
x = np.arange(0, 10*np.pi, 0.1)
y = np.sin(x)
#plotting to via the plot function in matplotlib.pyplot library
plt.plot(x, y, color='green')
plt.show()



