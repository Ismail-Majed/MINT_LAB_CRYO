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
Y=1
ENRfreq=np.array([0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 26.5])*1E9
ENRdb=np.array([15.64, 15.37, 14.89, 14.64, 14.47, 14.53, 14.7, 14.52, 14.32, 14.74, 15.60, 15.89, 15.68, 15.90, 16.58, 16.77, 16.57, 16.75, 16.78, 16.36, 15.95, 16.16, 16, 15.41, 14.74, 14.94, 15.2, 14.47, 14.46])


ENRlin=10**(ENRdb/10)
Thot=(ENRlin*T0)+Tcold
measfreq=np.linspace(1E8, 2E9, 201)
Thotinterp=np.interp(measfreq,ENRfreq,Thot)

# columns = ["A_1(DB)", "A_1(DEG)"]
# df = pd.read_csv("NoiseParam290k_A_1 .csv","A_1(DB)") 
# print(df)


df=pd.read_csv("NoiseParam290k_A_1 .csv")
print("The dataframe is:")
print(df)
specific_columns=df[["A_1(DB)","A_1(DEG)"]]
print("The column are:")
print(specific_columns)


network=rf.Network('./NoiseParam290k_B_2.s2p')
#result = numpy.empty([201,2])
#for i in range(67):
   # temp = cmath.polar(network.s[i,0,0])
    #print(temp)
#print(cmath.polar(network.s[:,0,0]))
#network.plot_s_db()

#Frec=(ENRlin-Y(Tcold/(T0-1)))/(Y-1)