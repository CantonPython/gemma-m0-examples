# Import Python libraries
from digitalio import DigitalInOut, Direction
import board
import time

# Set which colors are connected to which pins
blue = board.D2
red = board.D0
green = board.D1

# Define variables for each LED, and set the pin to digital input/output
led_blue = DigitalInOut(blue)
led_red = DigitalInOut(red)
led_green = DigitalInOut(green)

# Set each pin input/output direction to output
led_blue.direction = Direction.OUTPUT
led_red.direction = Direction.OUTPUT
led_green.direction = Direction.OUTPUT

# Loop this forever
while True:
    # Turn on blue LED
    led_blue.value = True
    # Wait 1/2 second
    time.sleep(1)
    # Turn off blue LED
    led_blue.value = False

    # Repeat for red LED
    led_red.value = True
    time.sleep(1)
    led_red.value = False

    # Repeat for green LED
    led_green.value = True
    time.sleep(1)
    led_green.value = False