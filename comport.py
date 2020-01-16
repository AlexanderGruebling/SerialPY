import sys
import serial
import threading


class ComPort(threading.Thread):

    ser = None
    data = []

    def get_ports(self):
        return serial.tools.list_ports.comports()

    def __init__(self, port, baud, timeout, byte, stop, parity):
        threading.Thread.__init__(self)
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.timeout = 1
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_TWO
        self.ser.parity = serial.PARITY_NONE
        self.ser.open()

    def read_from_com_port(self):
        RxData = ''
        while True:
            try:
                temp = self.ser.readline()
                RxData += str(temp)
                self.data += RxData
            except SyntaxError as e:
                print(e)
            continue

    def getReadData(self):
        return self.data

    def writeMessage(self, message):
        print('called')
        self.ser.write(message)
