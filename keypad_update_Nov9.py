#This is the updated keypad code for November 9, 2024

#Importing necessary classes for keypad code.

import lcddriver
import time
import digitalio
import board
import adafruit_matrixkeypad

class Keypad(lcddriver):
    
    def __init__(self):
        self.attempts=3
        self.reset_attempts=3
    
    def define_master_password(self):
        self.master_password_array=list()
        lcd_display.lcd_display_string('Set 6-Digit Password:')
        for index in range(6):
            self.master_number=int(input())
            self.master_password_array.append(self.master_number)
        while self.master_password_array == [0,0,0,0,0,0]:
            lcd_display.lcd_display_string('Invalid Password')
            lcd_display.lcd_display_string('Set 6-Digit Password:')
            for index in range(6):
                self.master_password_array.remove(0)
            for index in range(6):
                self.master_number=int(input())
                self.master_password_array.append(self.master_number)
                
    def enter_password(self):
        self.keypad_array=list()
        lcd_display.lcd_display_string('Enter 6-Digit Password:')
        for index in range(6):
            self.keypad_number=int(input())
            self.keypad_array.append(self.keypad_number)
            
    def verify_password(self):
        if self.keypad_array == self.master_password_array:
            self.keypad_array.clear()
            self.attempts=3
            lcd_display.lcd_display_string('Success!')
        elif self.keypad_array == [0,0,0,0,0,0]:
            self.keypad_reset_array=list()
            while self.reset_attempts > 0:
                lcd_display.lcd_display_string('Enter Current Password:')
                for index in range(6):
                    self.keypad_reset_number=int(input())
                    self.keypad_reset_array.append(self.keypad_reset_number)
                if self.keypad_reset_array == self.master_password_array:
                    self.reset_attempts=3
                    self.master_password_array.clear()
                    lcd_display.lcd_display_string('Enter New Password:')
                    for index in range(6):
                        self.master_number=int(input())
                        self.master_password_array.append(self.master_number)
                    while self.master_password_array == [0,0,0,0,0,0] or self.master_password_array == self.keypad_reset_array:
                        lcd_display.lcd_display_string('Invalid Password')
                        lcd_display.lcd_display_string('Set 6-Digit Password:')
                        self.master_password_array.clear()
                        for index in range(6):
                            self.master_number=int(input())
                            self.master_password_array.append(self.master_number)
                    break
                else:
                    self.reset_attempts=self.reset_attempts-1
                    if self.reset_attempts == 2:
                        self.keypad_reset_array.clear()
                        lcd_display.lcd_display_string('Try Again')
                        lcd_display.lcd_display_string('You have ' +str(int(self.reset_attempts))+ ' attempts before lock-out!')
                    elif self.reset_attempts == 1:
                        self.keypad_reset_array.clear()
                        lcd_display.lcd_display_string('Try Again')
                        lcd_display.lcd_display_string('You have ' +str(int(self.reset_attempts))+ ' attempt before lock-out!')
                    else:
                        self.keypad_reset_array.clear()
                        lcd_display.lcd_display_string('You have been locked out!')
        else:
              self.attempts=self.attempts-1
              if self.attempts == 2:
                  self.keypad_array.clear()
                  lcd_display.lcd_display_string('Try Again')
                  lcd_display.lcd_display_string('You have ' +str(int(self.attempts))+ ' attempts before lock-out')
              elif self.attempts == 1:
                  self.keypad_array.clear()
                  lcd_display.lcd_display_string('Try Again')
                  lcd_display.lcd_display_string('You have ' +str(int(self.attempts))+ ' attempt before lock-out')
              else:
                  self.keypad_array.clear()
                  lcd_display.lcd_display_string('You have been locked out!')
                  

#Main Program
                  
#Creating necessary values to integrate keypad
                
keypad_columns=[digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]

keypad_rows=[digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]

keypad_buttons=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

keypad_integration=adafruit_matrixkeypad.Matrix_Keypad(keypad_rows,keypad_columns,keypad_buttons)

keypad=Keypad()

lcd_display=lcddriver.lcd()

keypad.define_master_password()

while keypad.attempts > 0:
    
    keypad.enter_password()
    keypad.verify_password()
    
    if keypad.attempts == 0 or keypad.reset_attempts == 0:
        break