# Import Python libraries
import digitalio
import board
import time

# Set which colors are connected to which pins
blue = board.D2
red = board.D0
green = board.D1

# Define variables for each LED, and set the pin to digital input/output
led_blue = digitalio.DigitalInOut(blue)
led_red = digitalio.DigitalInOut(red)
led_green = digitalio.DigitalInOut(green)

# Set each pin input/output direction to output
led_blue.direction = digitalio.Direction.OUTPUT
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT

# Loop this forever
while True:
    # blue
    led_blue.value = True
    time.sleep(1)
    # purple
    led_red.value = True
    time.sleep(1)
    # red
    led_blue.value = False
    time.sleep(1)
    # yellow
    led_green.value = True 
    time.sleep(1)
    # green
    led_red.value = False
    time.sleep(1)
    # aqua
    led_blue.value = True
    time.sleep(1)
    led_blue.value = False
    led_green.value = False