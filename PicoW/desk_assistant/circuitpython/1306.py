# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2
# OLED DISPLAY: https://educ8s.tv/part/OLED096

import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import time 
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.line import Line


displayio.release_displays()


sda, scl = board.GP0, board.GP1

i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64, auto_refresh=True)
display.refresh()
# Make the display context
splash = displayio.Group()
display.show(splash)

# Make a background color fill
color_bitmap = displayio.Bitmap(128, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)
##############################

rect2 = Rect(0, 0, 128, 64, fill=0x000000, outline=0x0, stroke=3)
splash.append(rect2)

dnd_owner = label.Label(terminalio.FONT, text="DND", color=0xFFFFFF, x=10, y=10)
splash.append(dnd_owner)
call_owner = label.Label(terminalio.FONT, text="Call", color=0xFFFFFF, x=60, y=10)
splash.append(call_owner)
ok_owner = label.Label(terminalio.FONT, text="Ok", color=0xFFFFFF, x=115, y=10)
splash.append(ok_owner)
splash.append(Line(0, 19, 128, 19, 0xFFFFFF))
splash.append(Line(0, 50, 128, 50, 0xFFFFFF))


dnd_user = label.Label(terminalio.FONT, text="DND", color=0xFFFFFF, x=10, y=34)
splash.append(dnd_user)

connected_username = "sub: niraj"
connected_user = label.Label(terminalio.FONT, text=connected_username, color=0xFFFFFF, x=30, y=59)
splash.append(connected_user)

count = 0
while True:
#    text = "Value : {}".format(count)
#    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=28)
#    splash.append(text_area)
    time.sleep(1)
#    splash.remove(text_area)
    count = count + 1
