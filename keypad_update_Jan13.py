#1/13/25 Keypad Update

import time
import digitalio
import board
import adafruit_matrixkeypad
from RPLCD import CharLCD
import RPi.GPIO as GPIO

class Keypad():
    
    def __init__(self):
        self.attempts=3
        self.reset_attempts=3
        self.relay=Relay 
    
    def define_master_password(self):
        self.master_password_array=list()
        lcd_display.write_string(u'Set 6-Digit Password:')
        for index in range(6):
            self.master_number=int(input())
            self.master_password_array.append(self.master_number)
        while self.master_password_array == [0,0,0,0,0,0]:
            lcd_display.write_string(u'Invalid Password')
            lcd_display.write_string(u'Set 6-Digit Password:')
            for index in range(6):
                self.master_password_array.remove(0)
            for index in range(6):
                self.master_number=int(input())
                self.master_password_array.append(self.master_number)
                
    def enter_password(self):
        self.keypad_array=list()
        lcd_display.write_string(u'Enter 6-Digit Password:')
        for index in range(6):
            self.keypad_number=int(input())
            self.keypad_array.append(self.keypad_number)
            
    def verify_password(self):
        if self.keypad_array == self.master_password_array:
            self.keypad_array.clear()
            self.attempts=3
            lcd_display.write_string(u'Success!')
            GPIO.output(self.relay, GPIO.HIGH)
            time.sleep(20)
            GPIO.output(self.relay, GPIO.LOW) 
        elif self.keypad_array == [0,0,0,0,0,0]:
            self.keypad_reset_array=list()
            while self.reset_attempts > 0:
                lcd_display.write_string(u'Enter Current Password:')
                for index in range(6):
                    self.keypad_reset_number=int(input())
                    self.keypad_reset_array.append(self.keypad_reset_number)
                if self.keypad_reset_array == self.master_password_array:
                    self.reset_attempts=3
                    self.master_password_array.clear()
                    lcd_display.write_string(u'Enter New Password:')
                    for index in range(6):
                        self.master_number=int(input())
                        self.master_password_array.append(self.master_number)
                    while self.master_password_array == [0,0,0,0,0,0] or self.master_password_array == self.keypad_reset_array:
                        lcd_display.write_string(u'Invalid Password')
                        lcd_display.write_string(u'Set 6-Digit Password:')
                        self.master_password_array.clear()
                        for index in range(6):
                            self.master_number=int(input())
                            self.master_password_array.append(self.master_number)
                    break
                else:
                    self.reset_attempts=self.reset_attempts-1
                    if self.reset_attempts == 2:
                        self.keypad_reset_array.clear()
                        lcd_display.write_string(u'Try Again')
                        lcd_display.write_string(u'You have ' +str(int(self.reset_attempts))+ ' attempts before lock-out!')
                    elif self.reset_attempts == 1:
                        self.keypad_reset_array.clear()
                        lcd_display.write_string(u'Try Again')
                        lcd_display.write_string(u'You have ' +str(int(self.reset_attempts))+ ' attempt before lock-out!')
                    else:
                        self.keypad_reset_array.clear()
                        lcd_display.write_string(u'You have been locked out!')
        else:
              self.attempts=self.attempts-1
              if self.attempts == 2:
                  self.keypad_array.clear()
                  lcd_display.write_string(u'Try Again')
                  lcd_display.write_string(u'You have ' +str(int(self.attempts))+ ' attempts before lock-out')
              elif self.attempts == 1:
                  self.keypad_array.clear()
                  lcd_display.write_string(u'Try Again')
                  lcd_display.write_string(u'You have ' +str(int(self.attempts))+ ' attempt before lock-out')
              else:
                  self.keypad_array.clear()
                  lcd_display.write_string(u'You have been locked out!')
                  

#Main Program
                  
#Creating necessary values to integrate keypad
                
keypad_columns=[digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]

keypad_rows=[digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]

keypad_buttons=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

keypad_integration=adafruit_matrixkeypad.Matrix_Keypad(keypad_rows,keypad_columns,keypad_buttons)

lcd_display=CharLCD(cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

GPIO.setmode(GPIO.BCM)

Relay=12

GPIO.setup(Relay, GPIO.OUT)

keypad=Keypad()

keypad.define_master_password()

while keypad.attempts > 0:
    
    keypad.enter_password()
    keypad.verify_password()
    
    if keypad.attempts == 0 or keypad.reset_attempts == 0:
        break