import sys
import usb.core
import usb.util
import threading

class Endpoint(threading.Thread):

    def getUsbPort(self):
        return usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)

    def __init__(self, idVendor, idProduct):
        threading.Thread.__init__(self)
        self.idVendor = idVendor
        self.idProduct = idProduct
        self.data = []
        self.dev = self.getUsbPort()


    def readFromSerialPort(self, interface=0):
        # p rint(dev[0][(0,0)][0])
        # data = ""
        endpoint = self.dev[0][(0, 0)][0]

        self.dev.set_configuration()
        while True:
            try:
                temp = self.dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
                print(temp)
                self.data.append(temp)
            except usb.core.USBError as e:
                print(e)
        # if e.args == ('Operation timed out',):
            continue
        # release the device
        usb.util.release_interface(self.dev, interface)
        usb.util.dispose_resources(self.dev)
        #return data
        # reattach the device to the OS kernel
        # dev.attach_kernel_driver(interface)

