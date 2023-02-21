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

for dirs, files in os.walk('./Results'):
    #print(root)
    print(dirs[1])
    if(dirs[1].index('thru')):
        print(files)
   
    

# path_of_the_directory = './Results'
# name = ('thru','reflect','line')
# for files in os.listdir(path_of_the_directory):
#     if any(name) in files:
#         print(files)  
#     else:
#         continue


# directory = 'Results'
# files = Path(directory).glob('thru')
# for file in files:
#     print(file)

# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     T = rf.Network('./Results/thru/S-ParamMeas20k_thru.s2p')
#     R = rf.Network('./Results/reflect/S-ParamMeas20k_reflect.s2p')
#     L = rf.Network('./Results/line/S-ParamMeas20k_line.s2p')
    
#     media = rf.DefinedGammaZ0(frequency)
#     TRL= TRL(measured = [T, R, L])
    
#     error_network_out = TRL.error_ntwk[1]
#     #ask leo if ignore s22
#     Gave_out=error_network_out.s[:,1,0]**2
#     kBGtot=NoiseParamCode1_4.calculatereceiverGBK()*Gave_out
#     print(kBGtot)
    
