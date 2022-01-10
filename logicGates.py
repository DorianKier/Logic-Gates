def przywitanie():
    for i in range(3):
        GPIO.output(ledPin1, GPIO.HIGH)
        GPIO.output(ledPin2, GPIO.HIGH)
        sleep(.2)
        GPIO.output(ledPin1, GPIO.LOW)
        GPIO.output(ledPin2, GPIO.LOW)
        sleep(.2)

def onLed():
    GPIO.output(ledPin1, GPIO.HIGH)
    GPIO.output(ledPin2, GPIO.HIGH)

def offLed():
    GPIO.output(ledPin1, GPIO.LOW)
    GPIO.output(ledPin2, GPIO.LOW)

import Adafruit_BBIO.GPIO as GPIO
from time import sleep

ledPin1 = "P8_15"
ledPin2 = "P8_16"
buttonPin1 = "P8_11"
buttonPin2 = "P8_12"

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(buttonPin1, GPIO.IN)
GPIO.setup(buttonPin2, GPIO.IN)
print('=========== LOGIC_GATES.EXE ===========')
print(' ')
print('Tryby urzadzenia: AND, OR, XOR, NAND, NOR, XNOR')
mode=raw_input('Wpisz jaki tryb chcesz uruchomic: ')
przywitanie()
while(1):
    if mode == 'and':
        if GPIO.input(buttonPin1) and GPIO.input(buttonPin2):
            onLed()
        else:
            offLed()
    elif mode == 'nand':
        if GPIO.input(buttonPin1) and GPIO.input(buttonPin2):
            offLed()
        else:
            onLed()
    elif mode == 'or':
        if GPIO.input(buttonPin1) or GPIO.input(buttonPin2):
            onLed()
        else:
            offLed()
    elif mode == 'nor':
        if GPIO.input(buttonPin1) or GPIO.input(buttonPin2):
            offLed()
        else:
            onLed()
    elif mode == 'xor':
        if GPIO.input(buttonPin1) and GPIO.input(buttonPin2):
            offLed()
        elif GPIO.input(buttonPin1) or GPIO.input(buttonPin2):
            onLed()
        else:
            offLed()
    elif mode == 'xnor':
        if GPIO.input(buttonPin1) and GPIO.input(buttonPin2):
            onLed()
        elif GPIO.input(buttonPin1) or GPIO.input(buttonPin2):
            offLed()
        else:
            onLed()
    else:
        print('Nie ma takiego trybu! Uruchom ponowenie program.')
        break
    sleep(.2)
GPIO.cleanup()