
from digi.xbee.devices import XBeeDevice
device = XBeeDevice("COM6", 115200)
device.open()
device.send_data_broadcast("Al que este escuchando: Hello XBee Mundo!")
device.close()