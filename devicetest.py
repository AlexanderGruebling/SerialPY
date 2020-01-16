import sys

# myVendorId = 53769
# myProductId = 5377
# dev = usb.core.find()
# dev.set_configuration(1)
# for cfg in dev:
#    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
# print(dev.get_active_configuration())

# dev.set_configuration()
# test = dev.read(0x81,8)
# print ("res: ",test)
import sys
import glob
import serial

import serial.tools.list_ports
import serial

ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 9600
ser.timeout = 1
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.parity = serial.PARITY_NONE
print(ser)
ser.open()
ser.write(b'')

while True:
    ser.write(b'hello\n')
    print("hh")
    print(ser.readline().decode('utf-8'))
    continue
