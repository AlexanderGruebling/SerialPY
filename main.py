import sys
from tkinter import *
import _thread
import threading
from comport import ComPort

# global Settings
baudRate = 9600
dataBits = 8
stopBits = 2
parity = 1

dataList = []

serial = ComPort('COM4', baudRate, dataBits, 1, stopBits, 'N')
thread1 = threading.Thread(target=serial.read_from_com_port, args=())
print('kek')
thread1.start()
print('kek')

while True:
    dataList = serial.getReadData()
    serial.writeMessage(b"test")
    print(dataList)
    continue
