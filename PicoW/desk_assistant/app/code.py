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
from hid import InitiateAutopilot
from mqtt import InitializeMQTT
from adafruit_hid.mouse import Mouse
import usb_hid
displayio.release_displays()

username = "lan"
reciever_username = "niraj"

user_feed = "{}_feed".format(username)
reciever_feed ="{}_feed".format(reciever_username)

render_text = "ok"
render_text_x = 109

owner_auto = False
owner_ok = False
owner_dnd = False
owner_call = False


reciever_ok = False
reciever_dnd = False
reciever_call = False

render_requested = False

def initialize_display():

    sda, scl = board.GP0, board.GP1
    i2c = busio.I2C(scl, sda)

    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64, auto_refresh=True)
    display.refresh()
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(128, 64, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF
    bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    splash.append(bg_sprite)
    return splash


def render_initial_screen(splash):

    #making the complete screen black
    rect2 = Rect(0, 0, 128, 64, fill=0x000000, outline=0x0, stroke=3)
    splash.append(rect2)

    #rendering owner title bar
    dnd_owner = label.Label(terminalio.FONT, text="DND", color=0xFFFFFF, x=12, y=10)
    splash.append(dnd_owner)
    call_owner = label.Label(terminalio.FONT, text="Call", color=0xFFFFFF, x=57, y=10)
    splash.append(call_owner)
    ok_owner = label.Label(terminalio.FONT, text="Ok", color=0xFFFFFF, x=109, y=10)
    splash.append(ok_owner)

    #rendering seperating lines
    splash.append(Line(0, 19, 128, 19, 0xFFFFFF))
    splash.append(Line(0, 50, 128, 50, 0xFFFFFF))

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected! Listening for topic changes on %s" % reciever_feed)
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(reciever_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")


def message(client, topic, message):
    global reciever_ok
    global reciever_dnd
    global reciever_call
    global render_text
    global render_requested
    global render_text_x

    global owner_auto
    global owner_ok
    global owner_dnd
    global owner_call

    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))
    render_requested = True

    if message == "ok":
        render_text = "ok"
        render_text_x = 109
    elif message == "dnd":
        render_text = "dnd"
        render_text_x = 12
    elif message == "call":
        render_text = "call"
        render_text_x = 57



splash = initialize_display()
render_initial_screen(splash)

connected_username = "sub: niraj"
connected_user = label.Label(terminalio.FONT, text=connected_username, color=0xFFFFFF, x=30, y=59)
splash.append(connected_user)

mouse = Mouse(usb_hid.devices)
displacement = 100

mqtt_client = InitializeMQTT(connected,disconnected,message)
text_area = label.Label(terminalio.FONT, text="ok", color=0xFFFFFF, x=render_text_x, y=34)
splash.append(text_area)

print("Running the main loop")
count = 0
every_other = False
disable_autopilot = False
while True:
    mqtt_client.loop()

    if render_requested:
        splash.remove(text_area)
        text_area = label.Label(terminalio.FONT, text=render_text, color=0xFFFFFF, x=render_text_x, y=34)
        splash.append(text_area)
        render_requested = False
    count = count + 1
    mqtt_client.publish(user_feed, count)
    if disable_autopilot:
        if every_other:
            InitiateAutopilot(mouse,displacement)
            every_other = False
        else:
            InitiateAutopilot(mouse,displacement*-1)
            every_other = True
    time.sleep(1)

