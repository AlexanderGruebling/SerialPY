# import tkinter GUI library
from tkinter import *
import usb.core
import usb.util

# find our device
dev = usb.core.find()

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()

usb.util.find_descriptor(cfg, True, 1)
#intf = cfg[(0,0)]

#ep = usb.util.find_descriptor(dev, 1)

#assert ep is not None

# write the data
# ep.write('test')
window = Tk()

# set tkinter window name
window.title("Py Project")

# set tkinter window size
window.geometry('350x200')



# activate GUI Loop
window.mainloop()