from lakeshore import Model336
from lakeshore.model_336 import *
import time

def LakeshoreSetTemp(setPoint, outputNumber, range, deltaChuck, deltaChamber):
    tempOldB = 0
    tempOldC = 0
    tempOldD = 0
    done = 0
    errorVec = [0]*4
    cycleCount = 0

    myInstrument = Model336()
    myInstrument.set_display_setup(Model336DisplaySetupMode.ALL_INPUTS,Model336DisplayFieldsSize.LARGE,4)
    myInstrument.set_heater_setup(outputNumber,Model336HeaterResistance.HEATER_50_OHM, 1.0, Model336HeaterOutputUnits.POWER) 
    myInstrument.set_control_setpoint(outputNumber, setPoint)
    myInstrument.set_heater_range(outputNumber, range)
    myInstrument.set_control_setpoint(2, setPoint)
    myInstrument.set_heater_range(2, range)

    kelvinReadingA = myInstrument.get_kelvin_reading('A')
    kelvinReadingB = myInstrument.get_kelvin_reading('B')
    kelvinReadingC = myInstrument.get_kelvin_reading('C')
    kelvinReadingD = myInstrument.get_kelvin_reading('D')


    errorA = abs(kelvinReadingA - setPoint)
    errorB = abs(kelvinReadingB - tempOldB)
    errorC = abs(kelvinReadingC - tempOldC)
    errorD = abs(kelvinReadingD - tempOldD)

    while not (done):
        print("Set Point is :", setPoint)
        print("A: ",kelvinReadingA)
        print("B: ",kelvinReadingB)
        print("C: ",kelvinReadingC)
        print("D: ",kelvinReadingD,"\n\n")
        errorVec[0] = errorA>deltaChuck 
        errorVec[1] = errorB>deltaChamber
        errorVec[2] = errorC>deltaChamber 
        errorVec[3] = errorD>deltaChamber
        #print(errorVec)
        if (any(errorVec)):
            done = 0
            cycleCount = 0


            tempOldB = kelvinReadingB
            tempOldC = kelvinReadingC
            tempOldD = kelvinReadingD

            kelvinReadingA = myInstrument.get_kelvin_reading('A')
            kelvinReadingB = myInstrument.get_kelvin_reading('B')
            kelvinReadingC = myInstrument.get_kelvin_reading('C')
            kelvinReadingD = myInstrument.get_kelvin_reading('D')

            errorA = abs(kelvinReadingA - setPoint)
            errorB = abs(kelvinReadingB - tempOldB)
            errorC = abs(kelvinReadingC - tempOldC)
            errorD = abs(kelvinReadingD - tempOldD)
        else:
            kelvinReadingA = myInstrument.get_kelvin_reading('A')
            kelvinReadingB = myInstrument.get_kelvin_reading('B')
            kelvinReadingC = myInstrument.get_kelvin_reading('C')
            kelvinReadingD = myInstrument.get_kelvin_reading('D')

            errorA = abs(kelvinReadingA - setPoint)
            errorB = abs(kelvinReadingB - tempOldB)
            errorC = abs(kelvinReadingC - tempOldC)
            errorD = abs(kelvinReadingD - tempOldD)

            cycleCount += 1
            print(cycleCount, "/30 Cycles done")
            if(cycleCount == 30):
                done = 1
                print("DONE")
                return 
        time.sleep(30)



  

