import time
import board
import adafruit_dht
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
print(dhtDevice.temperature)
