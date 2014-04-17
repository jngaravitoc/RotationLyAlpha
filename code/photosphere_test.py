import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_in = np.loadtxt("../data/Homogeneous/V3005tHOM_in.ascii")
data_out = np.loadtxt("../data/Homogeneous/V3005tHOM_out.ascii")


nscatt = data_out[:,8]

x = data_in[:,0]
y = data_in[:,1]
z = data_in[:,2]

X = np.amax(x)
Y = np.amax(y)
Z = np.amax(z)

R = (X + Y + Z) /3.0

index_low = np.where(nscatt<100)
x_low = x[index_low]
y_low = y[index_low]
z_low = z[index_low]


index_high = np.where(nscatt>100)

x_high = x[index_high]
y_high = y[index_high]
z_high = z[index_high]

#print np.amax(x_high),np.amax(x_low)
#print len(x_high), len(x_low)
N =  float(len(nscatt))


r_low = np.sqrt(x_low**2 + y_low**2 + z_low**2)
r_high = np.sqrt(x_high**2 + y_high**2 + z_high**2)

hist_l, bin_edges_l = np.histogram(r_low)
hist_h, bin_edges_h = np.histogram(r_high)

plt.plot(bin_edges_l[:-1]/R, hist_l[:]/N, c = 'r', linewidth=2.5, label='Nscatt<100')
plt.plot(bin_edges_h[:-1]/R, hist_h[:]/N, c = 'g', linewidth=2.5, label=('Nscatt>100'))
plt.legend(loc='best')
plt.ylabel("Number of photons", fontsize=25)
plt.xlabel("Radius", fontsize=25)
plt.savefig("photosphere_test.png")
plt.show()

