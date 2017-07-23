import os
if os.name == 'nt':
        pass
        #from winusbpy import *
	#from winusb import *
else:
	raise ImportError("WinUsbPy only works on Windows platform")
