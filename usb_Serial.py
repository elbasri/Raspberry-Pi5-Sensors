import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(1)  # Allow some time for the serial connection to establish

try:
    while True:
        # Send command 'G'
        ser.write(b'G')
        print("Sent 'G'")
        time.sleep(0.100)  # Wait to see if a response is received
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after G:', response.decode())
        else:
            print('No response after G.')

        # Send command 'S'
        ser.write(b'S')
        print("Sent 'S'")
        time.sleep(1)  # Wait to see if a response is received
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after S:', response.decode())
        else:
            print('No response after S.')

        # Send command 'A'
        ser.write(b'A')
        print("Sent 'A'")
        time.sleep(1)  # Wait to see if a response is received
        if ser.in_waiting:
            response = ser.read(ser.in_waiting)
            print('Received after A:', response.decode())
        else:
            print('No response after A.')

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    ser.close()
    print("Serial connection closed.")
