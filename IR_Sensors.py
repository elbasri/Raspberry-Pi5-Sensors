import lgpio as GPIO
import time

# Define the GPIO pin
IR_PIN = 17  # Change as per your connection

# Open the GPIO chip and set the GPIO direction
h = GPIO.gpiochip_open(0)
GPIO.gpio_claim_input(h, IR_PIN)

def read_ir_sensor():
    # Read the IR sensor state
    state = GPIO.gpio_read(h, IR_PIN)
    return state

# Main program
if __name__ == '__main__':
    try:
        while True:
            if read_ir_sensor():
                print("IR Sensor Detected Something!")
            else:
                print("No Detection.")
            time.sleep(0.5)  # Delay for half a second

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.gpiochip_close(h)
