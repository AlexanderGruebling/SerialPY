import sys
import usb.core
import usb.util
from tkinter import *


dev = usb.core.find(idVendor=0x0461,idProduct=0x4d0f)
interface = 0
print(dev[0][(0,0)][0])
endpoint = dev[0][(0,0)][0]

dev.set_configuration()
while True:
    try:
        data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        print(data)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
# release the device
usb.util.release_interface(dev, interface)
usb.util.dispose_resources(dev)
# reattach the device to the OS kernel
# dev.attach_kernel_driver(interface)



window = Tk()

# set tkinter window name
window.title("PyTester")

# set tkinter window size
window.geometry('350x200')



# activate GUI Loop
window.mainloop()