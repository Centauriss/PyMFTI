import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, np.cos(x - 0.5))
#plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.show()