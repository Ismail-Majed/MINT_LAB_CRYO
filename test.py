from skrf import Network
import matplotlib.pyplot as plt

test = Network('C:/Users/labuser/Documents/LabSetup/Results/S-ParamMeas290k_testy.s2p')
test1 = Network('C:/Users/labuser/Documents/LabSetup/Results/S-ParamMeas290k_Z-Tuner-AW-O.s2p')
plt.subplot(211)
test.plot_s_db()
plt.subplot(212)
test1.plot_s_db()

plt.show()
