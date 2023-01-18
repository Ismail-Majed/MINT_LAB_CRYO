import keysight_ktna as inst
import numpy as np
import time
import datetime
import os



def initPNA(calSetID):
	resource_name = "USB0::0x2A8D::0x2B01::MY48420967::0::INSTR"
	id_query = True
	reset = False
	options = ""
	driver = inst.KtNA(resource_name, id_query, reset, options)


	print('  identifier: ', driver.identity.identifier)
	print('  revision:   ', driver.identity.revision)
	print('  vendor:     ', driver.identity.vendor)
	print('  description:', driver.identity.description)
	print('  model:      ', driver.identity.instrument_model)
	print('  resource:   ', driver.driver_operation.io_resource_descriptor)
	print('  options:    ', driver.driver_operation.driver_setup)

	print("\n")
	print("Basic Operations using IVI Native Commands")

	
	driver.system.factory_preset()
	driver.channels[0].apply_cal_set(calSetID, True)



def measSparam(temp, kind):

	driver.channels.delete_all_measurements()

	driver.display.windows.create_or_delete(True, 1)
	driver.display.windows.create_or_delete(True, 2)
	driver.display.windows.create_or_delete(True, 3)
	driver.display.windows.create_or_delete(True, 4)

	# # Create 1st Measurement
	driver.channels.add_measurement("S11", 1, 1)
	driver.display.windows[0].traces.feed_measurement_number(1, 1)

	# # Create 2nd Measurement
	driver.channels.add_measurement("S21", 2, 1)
	driver.display.windows[1].traces.feed_measurement_number(2, 1)

	driver.channels.add_measurement("S12", 3, 1) #Create a new Measurement
	driver.display.windows[2].traces.feed_measurement_number(3, 1) #Feed that measurement to a new trace

	driver.channels.add_measurement("S22", 4, 1) #Create a new Measurement
	driver.display.windows[3].traces.feed_measurement_number(4, 1) #Feed that measurement to a new trace

	driver.status.operation.enable_register = inst.StatusOperationFlags.AVERAGING_SUMMARY	
	driver.status.service_request_enable_register = inst.StatusByteFlags.OPERATION_SUMMARY
	driver.status.clear()
	#Trigger Channel

	driver.channels[0].averaging.enabled = 1
	driver.channels[0].averaging.factor = 128
	driver.channels[0].standard_stimulus.sweep.frequency.start = 100E6 #Initialize state
	driver.channels[0].standard_stimulus.sweep.frequency.stop = 2E9
	driver.channels[0].averaging.if_bandwidth = 1000

	driver.channels[0].standard_stimulus.sweep.trigger_mode = inst.SweepTriggerMode.CONTINUOUS

	while 1:
		time.sleep(1)
		status_byte = int(driver.status.read_status_byte_register())
		if(status_byte == 192)
			break
		pass
		


	# Measure and save S11
	data_Result1 = driver.channels[0].measurements[0].query_snp_data_for_specified_ports("1")
	driver.system.wait_for_operation_complete(datetime.timedelta(seconds = 10))
	# #driver.memory.save_trace_data("./NoiseParams/NoiseParam{}k.csv".format(temp),inst.keysight_ktna.TraceDataFileType.CSV_FORMATTED_DATA,inst.keysight_ktna.DataScope.TRACE,inst.keysight_ktna.DataFormat.RI,1)	
	driver.channels[0].measurements[0].save_snp_data("1 2", "./S-params/S-ParamMeas{}k.s2p".format(temp))
	driver.memory.upload_data("./S-params/S-ParamMeas{}k.s2p".format(temp),"C:/Users/labuser/Documents/LabSetup/Results/{}/S-ParamMeas{}k_{}.s2p".format(kind,temp,kind))
	#driver.memory.upload_data("./NoiseParams/NoiseParam{}k.csv".format(temp), "C:/Users/labuser/Documents/LabSetup/Results/{}/NoiseParam{}k_{}.csv".format(kind,temp,kind))
	driver.system.wait_for_operation_complete(datetime.timedelta(seconds = 100))



def measNoiseParam(temp, kind):

	driver.channels.delete_all_measurements()

	driver.display.windows.create_or_delete(True, 1)
	driver.display.windows.create_or_delete(True, 2)
	driver.display.windows.create_or_delete(True, 3)
	driver.display.windows.create_or_delete(True, 4)

	driver.channels.add_measurement("DUTNPD", 1, 1)
	driver.display.windows[0].traces.feed_measurement_number(1, 1)

	# # Create 2nd Measurement
	driver.channels.add_measurement("DUTNPDI", 2, 1)
	driver.display.windows[1].traces.feed_measurement_number(2, 1)

	driver.channels.add_measurement("SYSNPD", 3, 1) #Create a new Measurement
	driver.display.windows[2].traces.feed_measurement_number(3, 1) #Feed that measurement to a new trace

	driver.channels.add_measurement("SYSNPDI", 4, 1) #Create a new Measurement
	driver.display.windows[3].traces.feed_measurement_number(4, 1) #Feed that measurement to a new trace

	driver.status.operation.enable_register = inst.StatusOperationFlags.AVERAGING_SUMMARY	
	driver.status.service_request_enable_register = inst.StatusByteFlags.OPERATION_SUMMARY
	driver.status.clear()

	driver.channels[0].averaging.enabled = 1
	driver.channels[0].averaging.factor = 1024
	driver.channels[0].standard_stimulus.sweep.frequency.start = 100E6 #Initialize state
	driver.channels[0].standard_stimulus.sweep.frequency.stop = 2E9
	driver.channels[0].averaging.if_bandwidth = 1000

	driver.channels[0].standard_stimulus.sweep.trigger_mode = inst.SweepTriggerMode.CONTINUOUS

	while 1:
		time.sleep(1)
		status_byte = int(driver.status.read_status_byte_register())
		if(status_byte == 192)
			break
		pass
	
	driver.memory.save_trace_data("./NoiseParams/NoiseParam{}k.csv".format(temp),inst.keysight_ktna.TraceDataFileType.CSV_FORMATTED_DATA,inst.keysight_ktna.DataScope.TRACE,inst.keysight_ktna.DataFormat.RI,1)
	driver.system.wait_for_operation_complete(datetime.timedelta(seconds = 10))
	driver.memory.upload_data("./NoiseParams/NoiseParam{}k.csv".format(temp), "C:/Users/labuser/Documents/LabSetup/Results/{}/NoiseParam{}k_{}.csv".format(kind,temp,kind))
	driver.system.wait_for_operation_complete(datetime.timedelta(seconds = 100))
