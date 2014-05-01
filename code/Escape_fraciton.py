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
    nscatt = data[:,6]

    return kz, nscatt

def viewing_angle(filename, angle, distribution):
    kz, nscatt = reading_data(filename, distribution)
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
    
    nscatt01 = nscatt[index01]
    x1 = float(len(nscatt01))
    index = np.where(nscatt01==0)
    x2 = float(len(nscatt01[index]))
    ef01 = x2/x1 

    nscatt02 = x[index02]
    x1 = float(len(nscatt02))
    index = np.where(nscatt02==0)
    x2 = float(len(nscatt02[index]))
    ef02 = x2/x1

    nscatt03 = x[index03]
    x1 = float(len(nscatt03))
    index = np.where(nscatt03==0)
    x2 = float(len(nscatt03[index]))
    ef03 = x2/x1

    nscatt04 = x[index04]
    x1 = float(len(nscatt04))
    index = np.where(nscatt04==0)
    x2 = float(len(nscatt04[index]))
    ef04 = x2/x1

    nscatt05 = x[index05]
    x1 = float(len(nscatt05))
    index = np.where(nscatt05==0)
    x2 = float(len(nscatt05[index]))
    ef05 = x2/x1

    nscatt06 = x[index06]
    x1 = float(len(nscatt06))
    index = np.where(nscatt06==0)
    x2 = float(len(nscatt06[index]))
    ef06 = x2/x1
    
    nscatt07 = x[index07]
    x1 = float(len(nscatt07))
    index = np.where(nscatt07==0)
    x2 = float(len(nscatt07[index]))
    ef07 = x2/x1

    nscatt08 = x[index08]
    x1 = float(len(nscatt08))
    index = np.where(nscatt08==0)
    x2 = float(len(nscatt08[index]))
    ef08 = x2/x1

    nscatt09 = x[index09]
    x1 = float(len(nscatt09))
    index = np.where(nscatt09==0)
    x2 = float(len(nscatt09[index]))
    ef09 = x2/x1

    nscatt10 = x[index10]
    x1 = float(len(nscatt10))
    index = np.where(nscatt10==0)
    x2 = float(len(nscatt10[index]))
    ef10 = x2/x1
   
    
    if angle == 1:
        print ef01   
    
    if angle == 2:
        print ef02
    
    if angle == 3:
        print ef03
    
    if angle == 4:
        print ef04
    
    if angle == 5:
        print ef05
    
    if angle == 6:
        print ef06
    
    if angle == 7:
        print ef07
    
    if angle == 8:
        print ef08
    
    if angle == 9:
        print ef09
    
    if angle == 10:
        print ef10


filename = sys.argv[1]
angle = float(sys.argv[2])
distribution = float(sys.argv[3])
