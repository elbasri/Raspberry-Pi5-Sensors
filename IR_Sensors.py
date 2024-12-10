# IR_Sensors.py
# This script reads input from an infrared (IR) sensor to detect obstacles.
# It demonstrates real-time obstacle detection using GPIO on a Raspberry Pi.
# Tested on RPi5
## Author: ABDENNACER Elbasri (Twitter: @abdennacerelb | Linkedin @elbasri)

import lgpio as GPIO
import time

# تعريف المنفذ لمستشعر IR
# Define the GPIO pin
IR_PIN = 17  # Change as per your connection

# فتح شريحة GPIO وتحديد اتجاه GPIO
# Open the GPIO chip and set the GPIO direction
h = GPIO.gpiochip_open(0)
GPIO.gpio_claim_input(h, IR_PIN)

def read_ir_sensor():
    # قراءة حالة مستشعر IR
    # Read the IR sensor state
    state = GPIO.gpio_read(h, IR_PIN)
    return state

# البرنامج الرئيسي
# Main program
if __name__ == '__main__':
    try:
        while True:
            if read_ir_sensor():
                # كان هناك كشف
                # Detection occurred
                print("IR Sensor Detected Something!")
            else:
                # لا يوجد كشف
                # No detection
                print("No Detection.")
            time.sleep(0.5)  # تأخير لمدة نص ثانية

    # الإعادة بالضغط على CTRL + C
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.gpiochip_close(h)