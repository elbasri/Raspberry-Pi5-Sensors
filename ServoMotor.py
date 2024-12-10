from gpiozero import Servo
from time import sleep

# Set up parameters specific to the Futaba S3010
min_pulse_width = 0.0008  # 0.9ms
max_pulse_width = 0.0020  # 2.1ms

# Initialize the servo on GPIO 18
servo = Servo(18, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)

# Move the servo to one extreme
servo.min()
print("Servo at minimum position:", servo.value)
sleep(2)

# Move the servo to the other extreme
servo.max()
print("Servo at maximum position:", servo.value)
sleep(2)

# Center the servo
servo.mid()
print("Servo at middle position:", servo.value)
#servo.value = 1
#servo.value = 0
print("Servo at middle position:", servo.value)
sleep(50)

# Optionally, demonstrate gradual movement across the range
for value in range(-10, 11, 1):
    #servo.value = value / 10.0
    print(f"Servo at position: {servo.value}")
    sleep(0.1)
