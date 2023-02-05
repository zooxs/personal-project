import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(20, 2, 100)
x2 = np.random.normal(10, 1, 100)
u1 = (x1 - 20)/2
u2 = (x2 - 10)/1
X1, X2 = np.meshgrid(x1, x2)
U1, U2 = np.meshgrid(u1, u2)
Z = U1 - U2

plt.contour(U1, U2, Z)
plt.show()