import numpy as np
import sys

def reading_data(filename):
    data = np.loadtxt("../data/Homogeneous/"+filename)
    initpos=data[:,0]
    index_clean = np.where(~np.isnan(initpos))
    data = data[index_clean[0],:]
    X = data[:,0]
    Y = data[:,1]
    Z = data[:,2]
    kx = data[:,3]
    ky = data[:,4]
    kz = data[:,5]
    x = data[:,6]

    return X, Y, Z, kx, ky, kz, x

def viewing_section(filename):
    X, Y, Z, kx, ky, kz, x = reading_data(filename)
    ##k = np.cos((90-angle)*np.pi/180.)
    index1 = np.where(X<0)
    index1 = index1[0]
    index2 = np.where(X>0)
    index2 = index2[0]
    nbins =40
    ky1 = ky[index1]
    x1 = x[index1]
    ky2 = ky[index2]
    x2 = x[index2]
    comming = np.where(ky1>0)
    comming = comming[0]
    going = np.where(ky2>0)
    going = going[0]	
    xl = x1[comming] # l = left
    xr = x2[going] # r = right
    histl, binsl = np.histogram(xl, bins=nbins)
    histr, binsr = np.histogram(xr, bins=nbins)
	
    return histl, binsl, histr, binsr

filename = sys.argv[1]

histl, binsl, histr, binsr  = viewing_section(filename)

for i in range(len(histl)):
        print histl[i], binsl[i], histr[i], binsr[i]
                                    
