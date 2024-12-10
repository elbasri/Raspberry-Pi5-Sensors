
# Raspberry Pi 5 Sensors Integration

This repository contains scripts to connect and interact with various sensors and modules with a Raspberry Pi 5. Each script demonstrates the setup and usage of specific hardware components.

---
## Note:
Starting from Raspberry Pi 5, GPIO has moved from on-chip to the RP1 chip. 
This hardware change means libraries that access GPIO via memory-mapped registers might no longer work. It is recommended to use updated libraries like gpiozero for compatibility.
## ملاحظة:
اعتبارًا من Raspberry Pi 5، تم نقل واجهة GPIO من داخل الشريحة إلى شريحة RP1.
 هذا التغيير في العتاد يعني أن المكتبات التي تعتمد على الوصول إلى GPIO عبر السجلات المعتمدة على الذاكرة قد لا تعمل بعد الآن. يُوصى باستخدام مكتبات محدثة مثل gpiozero لضمان التوافق.


## 1. ServoMotor.py

### English:
This script controls a servo motor using GPIO pins on the Raspberry Pi. It uses the `gpiozero` library to define and manipulate the servo.

- **Setup**: Connect the servo signal wire to GPIO 18.
- **Functionality**: The servo moves to its minimum, maximum, and middle positions. It also demonstrates gradual movement.

### Arabic:
يتيح هذا السكربت التحكم في محرك سيرفو باستخدام منافذ GPIO في راسبيري باي. يستخدم مكتبة `gpiozero` لتعريف المحرك والتحكم به.

- **الإعداد**: قم بتوصيل سلك إشارة السيرفو بـ GPIO 18.
- **الوظيفة**: يتحرك السيرفو إلى أقصى اليسار، أقصى اليمين، والوسط. كما يتم عرض حركة تدريجية.

---

## 2. i2c_LCD_Arabic.py

### English:
This script interfaces with an I2C 16x2 LCD screen, supporting Arabic text display. Custom characters for Arabic must be added manually.

- **Setup**: Connect the I2C module to the Raspberry Pi.
- **Functionality**: Displays a static Arabic message on the LCD.

### Arabic:
يتفاعل هذا السكربت مع شاشة LCD من نوع I2C بحجم 16x2 ويدعم عرض النصوص باللغة العربية. يجب إضافة الحروف العربية يدويًا.

- **الإعداد**: قم بتوصيل وحدة I2C بـ راسبيري باي.
- **الوظيفة**: يعرض رسالة ثابتة باللغة العربية على الشاشة.

---

## 3. i2c_LCD.py

### English:
Similar to the Arabic version, this script communicates with an I2C LCD, supporting ASCII text and custom characters.

- **Setup**: Connect the I2C LCD module.
- **Functionality**: Sends and displays messages on the screen.

### Arabic:
مشابه للنسخة العربية، يتواصل هذا السكربت مع شاشة LCD من نوع I2C ويدعم الحروف الإنجليزية والحروف الخاصة.

- **الإعداد**: قم بتوصيل وحدة I2C LCD.
- **الوظيفة**: يرسل ويعرض الرسائل على الشاشة.

---

## 4. IR_Sensors.py

### English:
This script reads input from an IR sensor to detect obstacles.

- **Setup**: Connect the IR sensor to GPIO 17.
- **Functionality**: Outputs detection status in real-time.

### Arabic:
يقرأ هذا السكربت مدخلات مستشعر الأشعة تحت الحمراء لاكتشاف العوائق.

- **الإعداد**: قم بتوصيل مستشعر الأشعة تحت الحمراء بـ GPIO 17.
- **الوظيفة**: يعرض حالة الاكتشاف في الوقت الحقيقي.

---

## 5. usb_Serial.py

### English:
Communicates with external devices via USB serial. Demonstrates sending commands (`G`, `S`, `A`) and receiving responses.

- **Setup**: Connect a USB serial device to `/dev/ttyACM0`.
- **Functionality**: Sends commands and handles responses.

### Arabic:
يتواصل مع الأجهزة الخارجية عبر الاتصال التسلسلي USB. يعرض إرسال الأوامر (`G`, `S`, `A`) واستقبال الردود.

- **الإعداد**: قم بتوصيل جهاز USB تسلسلي بـ `/dev/ttyACM0`.
- **الوظيفة**: يرسل الأوامر ويتعامل مع الردود.

---

## 6. spiT.py

### English:
Uses the SPI interface to send structured data, demonstrating bidirectional communication.

- **Setup**: Connect the SPI device to the Raspberry Pi.
- **Functionality**: Sends a string ("Hello") using the SPI protocol.

### Arabic:
يستخدم واجهة SPI لإرسال بيانات مهيكلة، ويعرض الاتصال ثنائي الاتجاه.

- **الإعداد**: قم بتوصيل جهاز SPI بـ راسبيري باي.
- **الوظيفة**: يرسل نصًا ("Hello") باستخدام بروتوكول SPI.

---

## How to Run

1. Connect the respective hardware components as described.
2. Install the required Python libraries using pip:
   ```bash
   pip install gpiozero smbus lgpio spidev pyserial
   ```
3. Run the desired script:
   ```bash
   python3 script_name.py
   ```


## Author

Developed by **ABDENNACER Elbasri** | Twitter: **@abdennacerelb** | Linkedin **@elbasri**.