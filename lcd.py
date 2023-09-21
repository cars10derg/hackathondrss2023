#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "25aQ" # Change XYZ to the UID of your LCD 128x64 Bricklet

gezaehlteachsen1 = 0
gezaehlteachsen2 = 0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    lcd.clear_display()

    # Prüft ob Achsenwerte übereinstimmen (0,0= Line(max./7), Position(max. 21))
if gezaehlteachsen1 == gezaehlteachsen2:
     lcd.write_line(4, 3, "Zug vollstaendig") 
else:
    lcd.write_line(4,2, "zug unvollstandig!")
    lcd.wrrite_line(5,5, "Sofort halten!")


input("Press key to exit\n") # Use raw_input() in Python 2
ipcon.disconnect()