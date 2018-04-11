# Write your code here :-)# Import Python libraries
from digitalio import DigitalInOut, Direction, Pull
import board
import time

# Set which functions are connected to which pins
button_pin = board.D2
led_1_pin = board.D0
led_2_pin = board.D1

goal_counter = 0
goals = 3   

# Define variables for each LED or button,
# and set the pin to digital input/output
button = DigitalInOut(button_pin)
led_1 = DigitalInOut(led_1_pin)
led_2 = DigitalInOut(led_2_pin)

# Set each pin input/output direction to output
button.direction = Direction.INPUT
# Because the button is connected to Ground we use Pull.UP
button.pull = Pull.UP
led_1.direction = Direction.OUTPUT
led_2.direction = Direction.OUTPUT

while True:
    # Check if button is pressed
    goal_check = button.value
    if not goal_check:
        goal_counter += 1
        print("Button Pressed " + str(goal_counter) + " times!")
        led_1.value = True
        time.sleep(.5)
        led_1.value = False

    if goal_counter == goals:
        print("You made your goal!")
        # Flash lights 3 times if goals are met
        goal_counter = 0  # If you've reached your goal, restart the counter
        
        for x in range(0, 3):
            led_1.value = True
            time.sleep(.5)
            led_2.value = True
            time.sleep(.5)
            led_1.value = False
            time.sleep(.5)
            led_2.value = False
            led_1.value = True
            time.sleep(.5)
            led_2.value = True
            time.sleep(.5)
            led_1.value = False
            led_2.value = False
            
    time.sleep(0.1)  # delay to make check more reliable
