#!/usr/bin/python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""

from __future__ import print_function

import odrive
from odrive.enums import *
from odrive.utils import *
import time
import math
import signal
import sys


from configuration import *


DO_CALIBRATION = False
DO_CHECK_FAULT = True
DO_INITIAL_CONF = True



def poll_errors(drive):
    if my_drive.axis1.error:
        print("err found!!")
        return(True)

def check_fault(drive):
    if poll_errors(drive):
        dump_errors(drive, True)
        print("error cleared")




# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()

#my_drive=my_drive

# Find an ODrive that is connected on the serial port /dev/ttyUSB0
#my_drive = odrive.find_any("serial:/dev/ttyUSB0")

if DO_CHECK_FAULT:
    check_fault(my_drive)
    print("error cleared")

if DO_INITIAL_CONF:
    print("configuring, using index:", CONF_INDEX_SELECTOR)
    call_config(my_drive)



# Calibrate motor and wait for it to finish

if DO_CALIBRATION:
    print("starting calibration...")
    my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
    while my_drive.axis1.current_state != AXIS_STATE_IDLE:
        time.sleep(0.1)


my_drive.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
my_drive.axis1.controller.input_pos = my_drive.axis1.encoder.pos_abs

my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
while my_drive.axis1.current_state != AXIS_STATE_CLOSED_LOOP_CONTROL:
    time.sleep(0.5)
    print("waiting")
print("CLOSED LOOP CONTROL")
time.sleep(3)
# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")
# print("M1")
# my_drive.axis1.controller.move_incremental(8000, False)
# time.sleep(1)

# print("M2")
# my_drive.axis1.controller.move_incremental(0, False)
# time.sleep(1)

# print("M3")
# my_drive.axis1.controller.move_incremental(8000, False)

# dump_errors(my_drive)


# Or to change a value, just assign to the property
#my_drive.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL

print("Position setpoint is " + str(my_drive.axis1.controller.input_pos))



def signal_handler(sig, frame):
    my_drive.axis1.requested_state = AXIS_STATE_IDLE
    print('DISABLING MOTOR')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



#TODO declare command thread

#TODO declare monitor thread

#TODO? delcare print thread

###################################### START RUN #####################################

#TODO start threads

# A sine wave to test
t0 = time.monotonic()
cont =1000
while cont>0:
    if poll_errors(my_drive):
        print("bad things happened")
        break
    setpoint = 1.0 * math.sin((time.monotonic() - t0))*10
    print("goto " + str(setpoint))
    my_drive.axis1.controller.input_pos = setpoint
    time.sleep(0.01)
    cont=cont-1




my_drive.axis1.requested_state = AXIS_STATE_IDLE
# Some more things you can try:
if DO_CHECK_FAULT:
    check_fault(my_drive)
