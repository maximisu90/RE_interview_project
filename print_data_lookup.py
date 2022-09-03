import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('slit_energy_data.txt',skiprows=1)
print(data[:,:])

x=data[:,0]
y=data[:,1]

dx=x[1:]-x[:-1]
dy=y[1:]-y[:-1]

# plt.scatter(x,np.sqrt(np.log(y)))
plt.scatter(x,np.exp(y))
# plt.scatter(x,y)
# plt.yscale('log')
plt.show()