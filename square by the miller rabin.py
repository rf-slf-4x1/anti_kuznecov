import numpy as np
import matplotlib.pyplot as plt

a, b = -1.1, 1.1
e = 0.001
N = (b-a)*3/e**2
p = np.random.sample((int(N), 2))
p[:,1]*=3
p[:,0]=p[:,0]*(b-a)+a

x = np.linspace(a, b, 1024)
plt.plot(x,np.sin(x**2)+2, x, np.exp(x**2))

mask = np.logical_and(p[:,1]>np.exp(p[:,0]**2), p[:,1]<np.sin(p[:,0]**2)+2)

plt.plot(p[mask,0], p[mask,1], ',')

S = (b-a)*3*mask.sum()/mask.shape[0]
print(f'Площадь: {S}')

plt.show()