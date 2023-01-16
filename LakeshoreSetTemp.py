from lakeshore import Model336
from lakeshore.model_336 import *
import time
myInstrument = Model336()
myInstrument.set_display_setup(Model336DisplaySetupMode.ALL_INPUTS,Model336DisplayFieldsSize.LARGE,4)
myInstrument.set_heater_setup(1,Model336HeaterResistance.HEATER_50_OHM, 1.0, Model336HeaterOutputUnits.POWER)
set_point = 290
myInstrument.set_control_setpoint(1, set_point)
myInstrument.set_heater_range(1, Model336HeaterRange.HIGH)

kelvin_reading = myInstrument.get_kelvin_reading('B')
if (kelvin_reading < (set_point - 5)) or (kelvin_reading > (set_point + 5)):
    raise Exception("Temperature reading is not within 5k of the setpoint")

# Initiate autotune in PI mode, initial conditions will not be met if the system is not
# maintaining a temperature within 5 K of the setpoint
myInstrument.set_autotune('B', Model336AutoTuneMode.P_I)

# Poll the instrument until the autotune process completes
autotune_status = myInstrument.get_tuning_control_status()
while autotune_status["active_tuning_enable"] and not autotune_status["tuning_error"]:
    autotune_status = myInstrument.get_tuning_control_status()
    # Print the status to the console every 5 seconds
    print("Active tuning: " + str(autotune_status["active_tuning_enable"]))
    print("Stage status: " + str(autotune_status["stage_status"]) + "/10")
    time.sleep(5)

if autotune_status["tuning_error"]:
    raise Exception("An error occurred while running autotune")


