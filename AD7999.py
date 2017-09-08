# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD7999
# This code is designed to work with the MCP3428 4-20mA current receiver board available from ControlEverything.co
#https://www.controleverything.com/content/Analog-Digital-Converters?sku=AD7999_I2CADC
from OmegaExpansion import onionI2C
import time
DL = 0
DL1 = 0.01
# Get I2C bus
i2c = onionI2C.OnionI2C()
while True:
  data = [0x10]
  i2c.write(0x29, data)
  time.sleep(DL1)
 # AD7999 address, 0x29(41)
# Read data back, 2 bytes
# raw_adc MSB, raw_adc LSB
  data = i2c.readBytes(0x29, 0x00, 2)

# Convert the data to 8-bits
  raw_adc = ((data[0] & 0x0F) * 256 + (data[1] & 0xF0)) / 16

# Output data to screen
  print "Digital Value of Analog Input : %d" %raw_adc
  time.sleep(DL)
