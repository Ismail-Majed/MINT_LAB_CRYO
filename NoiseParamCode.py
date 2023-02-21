# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:18:08 2023
@author: marwa
"""
import numpy as np
import skrf as rf
import cmath
import pandas as pd
from pylab import *

T0=290
Tcold=295

ENRfreq=np.array([0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 26.5])*1E9
ENRdb=np.array([15.64, 15.37, 14.89, 14.64, 14.47, 14.53, 14.7, 14.52, 14.32,
14.74, 15.60, 15.89, 15.68, 15.90, 16.58, 16.77, 16.57, 16.75, 16.78,
16.36, 15.95, 16.16, 16, 15.41, 14.74, 14.94, 15.2, 14.47, 14.46])


measfreq=np.linspace(1E8, 2E9, 201)
interpolatedENRdb = np.interp(measfreq,ENRfreq,ENRdb)
ENRlin=10**(interpolatedENRdb/10)
Thot=(ENRlin*T0)+Tcold



Ncold_linear = [None] * 202
Nhot_linear = [None] * 202

noiseParamColdCSV = pd.read_csv("Results/NoiseSourceOFF/NoiseParam290k_B_2.csv",skiprows = 11,usecols =[1,2])
for index,row in enumerate(noiseParamColdCSV.iterrows()):
   complex_num = cmath.rect(10**(row[1][0]/10),2*pi*(row[1][1]/360))
   Ncold_linear[index] = complex_num * np.conj(complex_num)
   

noiseParamHotCSV = pd.read_csv("Results/NoiseSourceON/NoiseParam290k_B_2.csv",skiprows = 11,usecols =[1,2])
for index,row in enumerate(noiseParamHotCSV.iterrows()):
   complex_num = cmath.rect(10**(row[1][0]/10),2*pi*(row[1][1]/360))
   Nhot_linear[index] = complex_num * np.conj(complex_num)
   #print(Nhot_linear[index])
   #print(complex_num)
Nhot_linear.pop()
Ncold_linear.pop()

Y_factor = [None]*201
GPNA = [None]*201
TPNA = [None]*201
temp2 = T0*ENRlin
for i in range(200):
   Y_factor = Nhot_linear[i]/Ncold_linear[i]
   temp = Nhot_linear[i]-Ncold_linear[i]
   GPNA[i] = temp/temp2[i]
   TPNA[i] = (Ncold_linear[i]/GPNA[i])- Tcold
  # print(10*log10((TPNA[i]/T0)+1))



print(10*log10((ENRlin-Y_factor*((Tcold/T0)-1))/(Y_factor-1)))

