import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_one_state = GPIO.input(18)
    input_two_state = GPIO.input(23)
    input_three_state = GPIO.input(24)

    if input_one_state == True: 
	print('button one pressed')
    
    if input_two_state == True:
	print('button two pressed')

    if input_three_state == True:
	print('button three pressed')

   
