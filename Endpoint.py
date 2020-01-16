import sys
import serial
import threading

class Endpoint(threading.Thread):

    def getUsbPort(self):
        return usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)

    def __init__(self, idVendor, idProduct):
        threading.Thread.__init__(self)
        ser = serial.Serial()
        ser.port = 'COM4'
        ser.baudrate = 9600
        ser.timeout = 1
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE


    def readFromSerialPort(self, interface=0):
        # p rint(dev[0][(0,0)][0])
        # data = ""
        endpoint = self.dev[0][(0, 0)][2]

        self.dev.set_configuration()
        while True:
            try:
                #print( self.dev[0][(0, 0)][2])
                #print(self.dev..endpoint.out.end
                temp = self.dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
                #temp = self.dev.read(0x83, 0x40)
                #print(temp)
                #dataList.append(temp)
                #print(main.dataList)

                RxData = ''.join([chr(x) for x in temp])

                #print (RxData)
               # print(temp)

                self.data += RxData
                #self.data.append(RxData)
            except usb.core.USBError as e:
                print(e)
        # if e.args == ('Operation timed out',):
            continue
        # release the device
        usb.util.release_interface(self.dev, interface)
        usb.util.dispose_resources(self.dev)
        #return data
        # reattach the device to the OS kernel
        self.dev.attach_kernel_driver(interface)

    def getReadData(self):
        return self.data


    def writeMessage (self,message):


        # find our device
       # dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)

        # was it found?
        if self.dev is None:
            raise ValueError('Device not found')

        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.dev.set_configuration()

        # get an endpoint instance
        cfg = self.dev.get_active_configuration()
        intf = cfg[(0, 0)]

        ep = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match= \
                lambda e: \
                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                    usb.util.ENDPOINT_OUT)

        assert ep is not None

        # write the data
        ep.write(message)
