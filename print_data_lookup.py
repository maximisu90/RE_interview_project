import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
data=np.loadtxt('slit_energy_data.txt',skiprows=1)
# print(data[:,:])

x=data[:,0]
y=data[:,1]


f1=interp1d(x=x,y=1/y)
f2=interp1d(x=1/y,y=x)
print(round(1.65))
xl=np.linspace(10,150,300)
yl=np.linspace(3500,30000,300)
plt.scatter(x,y,c='k')
plt.plot(xl,1/f1(xl),c='r')
plt.plot(f2(1/yl),yl,c='b')
plt.show()