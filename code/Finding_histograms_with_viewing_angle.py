import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def reading_data(filename, distribution):
    if distribution == 0:
        data = np.loadtxt("../data/Homogeneous/"+filename)
    elif distribution ==1:
        data = np.loadtxt("../data/Central/"+filename)
    initpos=data[:,0]
    index_clean = np.where(~np.isnan(initpos))
    data = data[index_clean[0],:]
    kz = data[:,5]
    x = data[:,6]

    return kz, x

def viewing_angle(filename, angle, nbins, distribution):
    kz, x = reading_data(filename, distribution)
    index01 = np.where((abs(kz)<0.1))
    index02 = np.where((abs(kz)<0.2) & (abs(kz)>0.1))
    index03 = np.where((abs(kz)<0.3) & (abs(kz)>0.2))
    index04 = np.where((abs(kz)<0.4) & (abs(kz)>0.3))
    index05 = np.where((abs(kz)<0.5) & (abs(kz)>0.4))
    index06 = np.where((abs(kz)<0.6) & (abs(kz)>0.5))
    index07 = np.where((abs(kz)<0.7) & (abs(kz)>0.6))
    index08 = np.where((abs(kz)<0.8) & (abs(kz)>0.7))
    index09 = np.where((abs(kz)<0.9) & (abs(kz)>0.8))
    index10 = np.where((abs(kz)<1.0) & (abs(kz)>0.9))

    x01 = x[index01]
    x02 = x[index02]
    x03 = x[index03]
    x04 = x[index04]
    x05 = x[index05]
    x06 = x[index06]
    x07 = x[index07]
    x08 = x[index08]
    x09 = x[index09]
    x10 = x[index10]

    hist, bins = np.histogram(x, bins=nbins, normed=True)
    hist01, bins01 = np.histogram(x01, bins=nbins, normed=True)
    hist02, bins02 = np.histogram(x02, bins=nbins, normed=True)
    hist03, bins03 = np.histogram(x03, bins=nbins, normed=True)
    hist04, bins04 = np.histogram(x04, bins=nbins, normed=True)
    hist05, bins05 = np.histogram(x05, bins=nbins, normed=True)
    hist06, bins06 = np.histogram(x06, bins=nbins, normed=True)
    hist07, bins07 = np.histogram(x07, bins=nbins, normed=True)
    hist08, bins08 = np.histogram(x08, bins=nbins, normed=True)
    hist09, bins09 = np.histogram(x09, bins=nbins, normed=True)

    if angle == 1:
        for i in range(len(hist)):
		print hist01[i], bins01[i]

    if angle == 2:
        return hist02, bins02

    if angle == 3:
        return hist03, bins03

    if angle == 4:
        return hist04, bins04

    if angle == 5:
        return hist05, bins05

    if angle == 6:
        return hist06, bins06

    if angle == 7:
        return hist07, bins07

    if angle == 8:
        return hist08, bins08

    if angle == 9:
        return hist09, bins09

    if angle == 10:
        return hist10, bins10

filename = sys.argv[1]
angle = float(sys.argv[2])
bins = float(sys.argv[3])
mode = float(sys.argv[4])
distribution = float(sys.argv[5])

viewing_angle(filename, angle, bins, distribution)




