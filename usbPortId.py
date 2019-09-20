import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0461,idProduct=0x4d0f)
print(dev)
print("----------------------------------------")
print(dev[0][(0,0)][0])
print("----------------------------------------")
dev.is_kernel_driver_active(0)