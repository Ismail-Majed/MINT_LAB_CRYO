import importlib 
import sys
import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
from skrf.calibration import TRL
from math import e
import NoiseParamCode1_4
import glob, os
from pathlib import Path

frequency = rf.Frequency(start=100e6, stop=2e9, npoints=201, unit='Hz')
folders = ['thru','reflect','line']
temps = ['20k', '25k', '30k', '77k', '100k', '200k', '250k', '290k']
T = [None]*8
R = [None]*8 
L = [None]*8
for dirs in folders:
    innerdir = os.listdir("./Results/"+dirs)
    for file in innerdir:
        for i,temp in enumerate(temps):
            if(temp in file and folders[0] in file):
               T[i] = rf.Network("./Results/"+dirs+'/'+file)
            if(temp in file and folders[1] in file):
                R[i] = rf.Network("./Results/"+dirs+'/'+file)
            if(temp in file and folders[2] in file):
                L[i] = rf.Network("./Results/"+dirs+'/'+file)
media = rf.DefinedGammaZ0(frequency)
print (T[0])
for index, item in enumerate(T):
    trl= TRL(measured = [T[0], R[0], L[0]])
    error_network_out = trl.error_ntwk[1]
    Gave_out=error_network_out.s[:,1,0]**2
    kBGtot=NoiseParamCode1_4.calculatereceiverGBK()*Gave_out
    print(kBGtot)
   
# directory = './Results'

# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     T = rf.Network('./Results/thru/S-ParamMeas20k_thru.s2p')
#     R = rf.Network('./Results/reflect/S-ParamMeas20k_reflect.s2p')
#     L = rf.Network('./Results/line/S-ParamMeas20k_line.s2p')
#     print(T)
#     media = rf.DefinedGammaZ0(frequency)
#     trl= TRL(measured = [T, R, L])
#     error_network_out = trl.error_ntwk[1]
#     #ask leo if ignore s22
#     Gave_out=error_network_out.s[:,1,0]**2
#     kBGtot=NoiseParamCode1_4.calculatereceiverGBK()*Gave_out
#    # print(kBGtot)
    
