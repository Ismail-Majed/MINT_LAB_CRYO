import pyvisa
import sys
sys.path.append('C:\\Users\\Ismail\\Downloads\\hp662xa')
rm = pyvisa.ResourceManager()
instrument = rm.open_resource('GPIB0::12::INSTR')
 # Select +6V output


def turnOffOutput(outputNumber):
	instrument.write("OUT {} 0".format(outputNumber))


def setOutputV(outputNumber, voltage):
	instrument.write("OUT {} 1".format(outputNumber))
	instrument.write("VSET {} {}".format(outputNumber,voltage))
	print("Voltage on output {} has been changed to {}V".format(outputNumber,voltage))	


def setOutputI(outputNumber,current):
	instrument.write("OUT {} 1".format(outputNumber))
	instrument.write("ISET {} {}".format(outputNumber,current))
	print("Current limit on output {} has been changed to {}A".format(outputNumber,current))	

def setOutputIV(outputNumber, voltage, current):
	instrument.write("OUT {} 1".format(outputNumber))
	instrument.write("VSET {} {}".format(outputNumber,voltage))
	instrument.write("ISET {} {}".format(outputNumber,current))
	print("Current limit on output {} has been changed to {}A".format(outputNumber,current))
	print("Voltage on output {} has been changed to {}V".format(outputNumber,voltage))	

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
