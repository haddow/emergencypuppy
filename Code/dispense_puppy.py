#!/usr/bin/python3

from Adafruit_Thermal import *
from PIL import Image
import glob
import random
from gpiozero import Button

button = Button(17)

while True:
    button.wait_for_press()
    files = glob.glob('/home/pi/puppydispenser/images/*')

    img = Image.open(random.choice(files))

    printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=5)
    printer.println('\n\n')
    printer.printImage(img, True)
    printer.println('\n\n')
