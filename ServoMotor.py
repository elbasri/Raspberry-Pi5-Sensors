# ServoMotor.py
# This script controls a servo motor using GPIO on a Raspberry Pi.
# It demonstrates setting up, moving the servo to different positions, and gradual movement across its range.
# Tested on RPi5
## Author: ABDENNACER Elbasri (Twitter: @abdennacerelb | Linkedin @elbasri)

from gpiozero import Servo
from time import sleep

# تحديد المعايير لمحرك سيرفو من نوع Futaba S3010
# Set up parameters specific to the Futaba S3010
min_pulse_width = 0.0008  # 0.9ms
max_pulse_width = 0.0020  # 2.1ms

# تهيئة محرك السيرفو على GPIO 18
# Initialize the servo on GPIO 18
servo = Servo(18, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)

# نقل السيرفو إلى أحد المواقع القصوى
# Move the servo to one extreme
servo.min()
print("Servo at minimum position:", servo.value)
sleep(2)

# نقل السيرفو إلى الموقع المقابل 
# Move the servo to the other extreme
servo.max()
print("Servo at maximum position:", servo.value)
sleep(2)

# وضع السيرفو في الوسط
# Center the servo
servo.mid()
print("Servo at middle position:", servo.value)
sleep(50)

# خيارياً: عرض حركة تدريجية عبر المدى
# Optionally, demonstrate gradual movement across the range
for value in range(-10, 11, 1):
    #servo.value = value / 10.0
    print(f"Servo at position: {servo.value}")
    sleep(0.1)