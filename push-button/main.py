# Import Python libraries
from digitalio import DigitalInOut, Direction, Pull
import board
import time

# Set which colors are connected to which pins
switch_pin = board.D2
red = board.D0
green = board.D1

# Define variables for each LED, and set the pin to digital input/output
switch = DigitalInOut(switch_pin)
led_red = DigitalInOut(red)
led_green = DigitalInOut(green)

# Set each pin input/output direction to output
# and set switch to be True when button not pressed
switch.direction = Direction.INPUT
switch.pull = Pull.UP
led_red.direction = Direction.OUTPUT
led_green.direction = Direction.OUTPUT

while True:
    # Check if button is pressed
    if switch.value:
        led_red.value = True
        led_green.value = False
    else:
        led_green.value = True
        led_red.value = False
        time.sleep(1)

    time.sleep(0.01)  # delay to make check more reliable