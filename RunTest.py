from KeysightN5242B import *
from Agilent6626A import setOutputIV
from Agilent6626A import turnOffOutput
from LakeshoreTemp import LakeshoreSetTemp
from lakeshore import Model336
from lakeshore.model_336 import *
from skrf.vi import vna
import time

def setStateANoAtten():
	setOutputIV(2, 3.3, 0.1) #VDD
	setOutputIV(1, 0, 0.1) #sw1
	setOutputIV(4, 3.3, 0.1) #sw2
	setOutputIV(3, 0, 0.1) #atten
def setStateAWithAtten():
	setOutputIV(2, 3.3, 0.1) #VDD
	setOutputIV(1, 0, 0.1) #sw1
	setOutputIV(4, 3.3, 0.1) #sw2
	setOutputIV(3, 3.3, 0.1) #atten
def setStateB():
	setOutputIV(2, 3.3, 0.1) #VDD
	setOutputIV(1, 3.3, 0.1) #sw1
	setOutputIV(4, 3.3, 0.1) #sw2
	setOutputIV(3, 0, 0.1) #atten
def setStateC():
	setOutputIV(2, 3.3, 0.1) #VDD
	setOutputIV(1, 0, 0.1) #sw1
	setOutputIV(4, 0, 0.1) #sw2
	setOutputIV(3, 0, 0.1) #atten
def setStateD():
	setOutputIV(2, 3.3, 0.1) #VDD
	setOutputIV(1, 3.3, 0.1) #sw1
	setOutputIV(4, 0, 0.1) #sw2
	setOutputIV(3, 0, 0.1) #atten

tempList = [20,25,30,77,100,200,250,290]
# for temp in tempList:
	# turnOffOutput(1)
	# turnOffOutput(2)
	# turnOffOutput(3)
	# turnOffOutput(4)
	# LakeshoreSetTemp(temp,1,Model336HeaterRange.HIGH,0.1,0.5)
	# setStateAWithAtten()
	#measSparam(temp, "Receiver_AW")
measNoiseParam(20,"bingbong")
	# setStateANoAtten()
	# #measSparam(temp, "Receiver_AWO")
	# measNoiseParam(temp,"Receiver_AWO")
	# setStateB()
	# #measSparam(temp,"Receiver_B")
	# measNoiseParam(temp,"Receiver_B")
	# setStateC()
	# #measSparam(temp, "Receiver_C")
	# measNoiseParam(temp,"Receiver_C")
	# setStateD()
	# #measSparam(temp, "Receiver_D")
	# measNoiseParam(temp,"Receiver_D")

	# turnOffOutput(1)
	# turnOffOutput(2)
	# turnOffOutput(3)
	# turnOffOutput(4)
