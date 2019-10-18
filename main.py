import sys
import usb.core
import usb.util
from tkinter import *
import _thread
import threading
from Operations import to_hex, to_ascii
from Endpoint import Endpoint

# global Settings
idVendor = 0x0738
idProduct = 0x1703
baudRate = 9600
dataBits = 8
stopBits = 1
parity = 1

endpoint = Endpoint(idVendor, idProduct)
#endpoint.readFromSerialPort(0)

# _thread.start_new_thread(endpoint.readFromSerialPort)

thread1 = threading.Thread(target=endpoint.readFromSerialPort, args=(0,))
thread1.start()

print("test")
print(to_hex(10))
print(to_ascii(97))
#dev = usb.core.find(idVendor=idVendor, idProduct=idProduct) #idVendor=0x0461,idProduct=0x4d0f
#interface = 0
#print(dev[0][(0,0)][0])
#endpoint = dev[0][(0,0)][0]

#dev.set_configuration()
#while True:
 #   try:
  #      data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
   #     print(data)
    #except usb.core.USBError as e:
     #   if e.args == ('Operation timed out',):
      #      continue
# release the device
#usb.util.release_interface(dev, interface)
#usb.util.dispose_resources(dev)
# reattach the device to the OS kernel
# dev.attach_kernel_driver(interface)



