import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
f=250;fs=10000;
s=0.5*np.cos(2*np.pi*f/fs*n+np.pi/2)
#plt.plot(n,s);plt.show()
plt.stem(n,s);plt.show()


