#Second Iteration of Code
#MAKE SURE INIT HAS TWO _ ON EACH END!
#Goal 1: Create the verification process (Complete)
#Goal 2: Let the user define their password (Complete)
#Goal 3: Make lock-out counter functional (Complete)
#Goal 4: Create reset password condition (Complete)
#Goals 5 to 7 are my main goal to finish (particularly number 5) plus the barcode scanner
#Goal 5: Integrate code with physical keypad and display
#Goal 6: Store user-defined password somehow?
#Password: have a default password to store password 
#Goal 7: Create lock-out timer
#Goal Overall: Debug and Optimize Code


#Importing Necessary Classes for LCD Display and Keypad Integration

import lcddriver
import time
import digitalio
import board
import adafruit_matrixkeypad


#Defining the Keypad class

class Keypad:
    
    def __init__(self):
        self.password=None
        self.attempts=3
        self.reset_attempts=3
        self.entered_password=None
        self.reset_password=None
        
    def user_define_password(self):
        lcd_display.lcd_display_string('Enter user-defined password:')
        self.defined_password=input()
        while int(self.defined_password) == 000000:
            lcd_display.lcd_display_string('Invalid Password! Please type new password!')
            lcd_display.lcd_display_string('Enter user-defined password:')
            self.defined_password=input()
        
    def user_enter_password(self):
        lcd_display.lcd_display_string('Enter keypad password:')
        self.entered_password=input()
        
    def verify_password(self):
        if int(self.entered_password)==int(self.defined_password):
            self.attempts=3
            lcd_display.lcd_display_string('Success! Box is Open!')
            
        elif int(self.entered_password) == 000000:
            lcd_display.lcd_display_string('Reset User-Defined Password')
            self.attempts=3
            while self.reset_attempts > 0:
                self.reset_password=input('Enter previous password:')
                if int(self.reset_password) == int(self.defined_password):
                    self.reset_attempts=3
                    self.defined_password=int(input('Enter new user-defined password:'))
                    while int(self.defined_password) == 000000 or int(self.defined_password) == int(self.reset_password):
                        lcd_display.lcd_display_string('Invalid Password! Please type new password:')
                        self.defined_password=int(input('Enter new user-defined password:'))
                    break
                else:
                    self.reset_attempts=self.reset_attempts-1
                    if self.reset_attempts == 2:
                        lcd_display.lcd_display_string('Try Again!')
                        lcd_display.lcd_display_string('You have ' +str(int(self.reset_attempts))+ ' attempts left before being locked out!')
                    elif self.reset_attempts == 1:
                        lcd_display.lcd_display_string('Try Again!')
                        lcd_display.lcd_display_string('You have ' +str(int(self.reset_attempts))+ ' attempt left before being locked out!')
                    else:
                        lcd_display.lcd_display_string('Locked Out!')
            
        else:
            self.attempts=self.attempts-1
            if self.attempts == 2:
                lcd_display.lcd_display_string('Try Again!')
                lcd_display.lcd_display_string('You have ' +str(int(self.attempts))+ ' attempts left before being locked out!')
            elif self.attempts == 1:
                lcd_display.lcd_display_string('Try Again')
                lcd_display.lcd_display_string('You have ' +str(int(self.attempts))+ ' attempt left before being locked out!')
            else:
                lcd_display.lcd_display_string('Locked Out!')

            

#Main Loop/Program
                
#Creating necessary values to integrate keypad
                
keypad_columns=[digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]

keypad_rows=[digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]

keypad_buttons=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

keypad_integration=adafruit_matrixkeypad.Matrix_Keypad(keypad_rows,keypad_columns,keypad_buttons)

#Creating keypad and lcd_display classes for main loop
                     
keypad=Keypad()

lcd_display=lcddriver.lcd()

#This is the main while loop to enter and reset password with keypad

keypad.user_define_password()

while keypad.attempts> 0:
    
    keypad.user_enter_password()
    keypad.verify_password()
    
    if keypad.attempts == 0 or keypad.reset_attempts == 0:
        break
    
