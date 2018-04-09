from digitalio import DigitalInOut, Direction
import board
import time

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
while True:
    led.value = not led.value
    time.sleep(1)