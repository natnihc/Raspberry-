import RPi.GPIO as GPIO
import time
# Set GPIO mode
GPIO.setmode(GPIO.BCM)
# Define the GPIO pin for the LDR
LDR_PIN = 17 # Change to the appropriate GPIO pin
# Initialize GPIO settings
GPIO.setup(LDR_PIN, GPIO.IN)
# Define a function to measure light levels
def rc_time(LDR_PIN):
count = 0
GPIO.setup(LDR_PIN, GPIO.OUT)
GPIO.output(LDR_PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.setup(LDR_PIN, GPIO.IN)
while GPIO.input(LDR_PIN) == GPIO.LOW:
count += 1
return count
try:
print("Light Level Detection. Press Ctrl+C to exit.")
while True:
light_duration = rc_time(LDR_PIN)
if light_duration >= 50000:
print("Dark (Low Light)")
elif light_duration < 10000:
print("Bright (High Light)")
else:
print("Moderate Light")
time.sleep(1) # Update the measurement every 1 second
except KeyboardInterrupt:
print("Light level detection stopped.")
GPIO.cleanup()
