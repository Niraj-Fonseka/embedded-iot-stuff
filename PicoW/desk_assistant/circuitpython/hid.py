# Write your code here :-)
import time
import analogio
import board
import digitalio
import usb_hid




def InitiateAutopilot(mouse,displacement):
    mouse.move(x=displacement)
