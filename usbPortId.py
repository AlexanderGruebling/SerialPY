import usb.core
import usb.util

# find our device
dev = usb.core.find()
print(dev)
#print("----------------------------------------")
#print(dev[0][(0,0)][0])
#print("----------------------------------------")
#dev.is_kernel_driver_active(0)