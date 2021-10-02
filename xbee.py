
from digi.xbee.devices import XBeeDevice
device = XBeeDevice("COM6", 115200)
device.open()
device.send_data_broadcast("Nuevo mensaje: Hello XBee TODOS!")
device.close()