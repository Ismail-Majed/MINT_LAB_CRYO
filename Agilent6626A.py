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

