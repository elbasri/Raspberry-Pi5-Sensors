# usb_Serial.py
# This script demonstrates communication with external devices using USB serial on a Raspberry Pi.
# It sends commands and handles responses, showcasing serial interaction.
# Tested on RPi5
## Author: ABDENNACER Elbasri (Twitter: @abdennacerelb | Linkedin @elbasri)

import serial
import time

# إنشاء اتصال تسلسلي
# Establish a serial connection
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(1)  # إفساح الوقت لإنشاء الاتصال

try:
    while True:
        # إرسال الأمر 'G'
        # Send command 'G'
        ser.write(b'G')
        print("Sent 'G'")
        time.sleep(0.100)  # الانتظار لمعرفة ما إذا كانت هناك استجابة
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after G:', response.decode())
        else:
            print('No response after G.')

        # إرسال الأمر 'S'
        # Send command 'S'
        ser.write(b'S')
        print("Sent 'S'")
        time.sleep(1)  # الانتظار لمعرفة ما إذا كانت هناك استجابة
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after S:', response.decode())
        else:
            print('No response after S.')

        # إرسال الأمر 'A'
        # Send command 'A'
        ser.write(b'A')
        print("Sent 'A'")
        time.sleep(1)  # الانتظار لمعرفة ما إذا كانت هناك استجابة
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after A:', response.decode())
        else:
            print('No response after A.')

except KeyboardInterrupt:
    # إيقاف البرنامج من قبل المستخدم
    # Program terminated by user
    print("Program terminated by user.")

finally:
    # إغلاق الاتصال التسلسلي
    # Close the serial connection
    ser.close()
    print("Serial connection closed.")
