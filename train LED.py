import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Pin0 = 8
Pin1 = 10
Pin2 = 12
Pin3 = 16
GPIO.setup(Pin0, GPIO.OUT)
GPIO.output(Pin0, GPIO.HIGH)
sleep(1)
GPIO.output(Pin0, GPIO.LOW)
GPIO.output(Pin1, GPIO.HIGH)
sleep(1)
GPIO.output(Pin1, GPIO.LOW)
GPIO.output(Pin2, GPIO.HIGH)
sleep(1)
GPIO.output(Pin2, GPIO.LOW)
GPIO.output(Pin3, GPIO.HIGH)
sleep(1)
GPIO.output(Pin3, GPIO.LOW)
GPIO.output(Pin2, GPIO.HIGH)
sleep(1)
GPIO.output(Pin2, GPIO.LOW)
GPIO.output(Pin1, GPIO.HIGH)
sleep(1)
GPIO.output(Pin1, GPIO.LOW)
GPIO.output(Pin0, GPIO.HIGH)
sleep(1)²
GPIO.output(Pin0, GPIO.LOW)
sleep(1)