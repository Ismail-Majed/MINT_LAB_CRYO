import sys
import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
from skrf.calibration import TRL
from math import e

frequency = rf.Frequency(start=100e6, stop=2e9, npoints=201, unit='Hz')

T = rf.Network('./Results/thru/S-ParamMeas20k_thru.s2p')
R = rf.Network('./Results/reflect/S-ParamMeas20k_reflect.s2p')
L = rf.Network('./Results/line/S-ParamMeas20k_line.s2p')

media = rf.DefinedGammaZ0(frequency)
TRL= TRL(measured = [T, R, L])

#error_network_in = TRL.error_ntwk[0]
error_network_out = TRL.error_ntwk[1]
error_network_out.plot_s_db()
#ask leo if ignore s22
Gave_out=error_network_out.s[:,1,0]**2
print(Gave_out)
#error_network_in.plot_s_db()


# delayList = [-350,-400,-450,-500,-550]

# for delay in delayList:
# 	dut_raw = rf.Network('./Results/ZTunerD/S-ParamMeas20k_ZTunerD.s2p')
# 	dut_corrected = TRL.apply_cal(dut_raw)
# 	dut_corrected = dut_corrected.delay(delay,unit = 'ps', port =1)
# 	dut_corrected.plot_s_smith(m = 1, n = 1, label = 'S22_StateD')

	
# 	dut_raw2 = rf.Network('./Results/ZTunerC/S-ParamMeas20k_ZTunerC.s2p')
# 	dut_corrected2 = TRL.apply_cal(dut_raw2)
# 	dut_corrected2 = dut_corrected2.delay(delay,unit = 'ps', port =1)
# 	dut_corrected2.plot_s_smith(m = 1, n = 1, label = 'S22_StateC')

# 	dut_raw3 = rf.Network('./Results/ZTunerB/S-ParamMeas20k_ZTunerB.s2p')
# 	dut_corrected3 = TRL.apply_cal(dut_raw3)
# 	dut_corrected3 = dut_corrected3.delay(delay,unit = 'ps', port =1)
# 	dut_corrected3.plot_s_smith(m = 1, n = 1, label = 'S22_StateB')
# 	# dut_corrected1.plot_s_smith(m = 1, n = 1, label = 'S22_Delay')
# 	plt.axis([-1.1,2.1,-1.1,1.1])
plt.show()