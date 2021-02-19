import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Pin = 8
GPIO.setup(Pin, GPIO.OUT)
for i in range (5) :
    GPIO.output(Pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(Pin, GPIO.LOW)
    sleep(1)

