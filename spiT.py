import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI port 0, device (chip select) 0
spi.max_speed_hz = 50000

try:
    while True:  # Infinite loop to keep sending the data
        # Start character for structured data
        spi.xfer2([ord('<')])  # Send start character
        for char in "Hello":
            data = spi.xfer2([ord(char)])  # Convert char to ASCII and send
            print("Sent:", char)
            time.sleep(0.1)  # Short delay between characters
        # End character for structured data
        spi.xfer2([ord('>')])  # Send end character
        print("String sent. Sending again...")
        time.sleep(1)  # Delay before sending the string again

finally:
    spi.close()  # Ensure SPI is closed on exit
