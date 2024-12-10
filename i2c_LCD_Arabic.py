# i2c_LCD_Arabic.py
# This script interfaces with a 16x2 LCD screen using I2C protocol to display Arabic text.
# It demonstrates initialization, sending commands, and displaying messages on the LCD.
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

# عناوين قواعدية لخطوط LCD 16x2
# Base addresses for lines on a 16x2 LCD
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# تأخيرات الزمن
# Time delays
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
    # تهيئة الشاشة
    # Initialize display
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Initialize
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Display On, Cursor Off, Blink Off 
    lcd_byte(0x28, LCD_CMD)  # Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # Clear display
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
    # إرسال النصوص للشاشة
    # Send string to display
    message = message.ljust(16, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(16):
        lcd_byte(ord(message[i]), LCD_CHR)

def display_arabic():
    # النصوص العربية يجب تعريفها هنا
    # Custom characters need to be defined here. This is an example for standard ASCII.
    # You will need to replace this part with your custom Arabic character codes.
    lcd_string("TajTech MDS", LCD_LINE_1)
    lcd_string("MundiaPolis University", LCD_LINE_2)

if __name__ == '__main__':
    lcd_init()
    display_arabic()