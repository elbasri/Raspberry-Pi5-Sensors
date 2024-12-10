# i2c_LCD.py
# This script interfaces with a 16x2 LCD screen using I2C protocol to display ASCII and custom characters.
# It demonstrates initialization, custom character creation, and displaying messages on the LCD.
# Tested on RPi5
## Author: ABDENNACER Elbasri (Twitter: @abdennacerelb | Linkedin @elbasri)

import smbus
import time

# تعريف منفذ I2C
# Define the I2C bus
bus = smbus.SMBus(1)

# عنوان شاشة LCD
# LCD I2C address
address = 0x27

# تعريف الوضعيات للبيانات والأوامر
# Commands
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

# عناوين الخطوط في شاشة LCD 16x2
# Base addresses for lines on a 16x2 LCD
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# مدد التأخير
# Time delays
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
    # تهيئة الشاشة
    # Initialize display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialize
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialize
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off 
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    # إرسال بتات للشاشة
    # Send byte to data pins
    bits_high = mode | (bits & 0xF0) | 0x08
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08

    # High bits
    bus.write_byte(address, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(address, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # تفعيل التوضيح
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(address, (bits | 0x04))
    time.sleep(E_PULSE)
    bus.write_byte(address, (bits & ~0x04))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # إرسال رسالة نصية إلى الشاشة
    # Send string to display
    message = message.ljust(16, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(16):
        lcd_byte(ord(message[i]), LCD_CHR)

# تعريف الحروف المخصصة
# Define custom character
custom_char = [
    0b00000,
    0b01010,
    0b01010,
    0b01010,
    0b10001,
    0b10001,
    0b01110,
    0b00000
]

def create_custom_char(location, charmap):
    # إنشاء حرف مخصص وتحميله للشاشة
    # Create and upload a custom character
    lcd_byte(0x40 + (location * 8), LCD_CMD)
    for i in charmap:
        lcd_byte(i, LCD_CHR)

if __name__ == '__main__':
    # الكتلة الرئيسية للبرنامج
    # Main program block
    lcd_init()
    # Upload custom character to LCD
    create_custom_char(0, custom_char)

    # To display the custom character, reference its location
    lcd_byte(0, LCD_CHR)  # Displays the custom character stored at location 0
