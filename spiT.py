# spiT.py
# This script demonstrates SPI communication on a Raspberry Pi.
# It sends structured data, including start and end characters, using the SPI protocol.
# Tested on RPi5
## Author: ABDENNACER Elbasri (Twitter: @abdennacerelb | Linkedin @elbasri)

import spidev
import time

# فتح منفذ SPI وتعيين الجهاز والسرعة
# Open SPI port and set device and speed
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI port 0, device (chip select) 0
spi.max_speed_hz = 50000

try:
    while True:  # دالة تكرار لارسال البيانات بشكل مستمر
        # Infinite loop to keep sending the data

        # رمز البداية للبيانات المنسقة
        # Start character for structured data
        spi.xfer2([ord('<')])  # Send start character

        for char in "Hello":
            # إرسال حرف تلو الآخر
            # Convert char to ASCII and send
            data = spi.xfer2([ord(char)])
            print("Sent:", char)
            time.sleep(0.1)  # تأخير قصير بين الحروف

        # رمز النهاية للبيانات المنسقة
        # End character for structured data
        spi.xfer2([ord('>')])  # Send end character
        print("String sent. Sending again...")

        time.sleep(1)  # تأخير قبل إعادة إرسال السلسلة

finally:
    # التأكد من إغلاق SPI عند الخروج
    # Ensure SPI is closed on exit
    spi.close()