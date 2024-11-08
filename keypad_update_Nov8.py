#This is the updated keypad code for November 8, 2024

class Keypad:
    
    def __init__(self):
        self.attempts=3
        self.reset_attempts=3
    
    def define_master_password(self):
        self.master_password_array=list()
        print('Set 6-Digit Password:')
        for index in range(6):
            self.master_number=int(input())
            self.master_password_array.append(self.master_number)
        while self.master_password_array == [0,0,0,0,0,0]:
            print('Invalid Password')
            print('Set 6-Digit Password:')
            for index in range(6):
                self.master_password_array.remove(0)
            for index in range(6):
                self.master_number=int(input())
                self.master_password_array.append(self.master_number)
                
    def enter_password(self):
        self.keypad_array=list()
        print('Enter 6-Digit Password:')
        for index in range(6):
            self.keypad_number=int(input())
            self.keypad_array.append(self.keypad_number)
            
    def verify_password(self):
        if self.keypad_array == self.master_password_array:
            self.keypad_array.clear()
            self.attempts=3
            print('Success!')
        elif self.keypad_array == [0,0,0,0,0,0]:
            self.keypad_reset_array=list()
            while self.reset_attempts > 0:
                print('Enter Current Password:')
                for index in range(6):
                    self.keypad_reset_number=int(input())
                    self.keypad_reset_array.append(self.keypad_reset_number)
                if self.keypad_reset_array == self.master_password_array:
                    self.reset_attempts=3
                    self.master_password_array.clear()
                    print('Enter New Password:')
                    for index in range(6):
                        self.master_number=int(input())
                        self.master_password_array.append(self.master_number)
                    while self.master_password_array == [0,0,0,0,0,0] or self.master_password_array == self.keypad_reset_array:
                        print('Invalid Password')
                        print('Set 6-Digit Password:')
                        self.master_password_array.clear()
                        for index in range(6):
                            self.master_number=int(input())
                            self.master_password_array.append(self.master_number)
                    break
                else:
                    self.reset_attempts=self.reset_attempts-1
                    if self.reset_attempts == 2:
                        self.keypad_reset_array.clear()
                        print('Try Again')
                        print('You have ' +str(int(self.reset_attempts))+ ' attempts before lock-out!')
                    elif self.reset_attempts == 1:
                        self.keypad_reset_array.clear()
                        print('Try Again')
                        print('You have ' +str(int(self.reset_attempts))+ ' attempt before lock-out!')
                    else:
                        self.keypad_reset_array.clear()
                        print('You have been locked out!')
        else:
              self.attempts=self.attempts-1
              if self.attempts == 2:
                  self.keypad_array.clear()
                  print('Try Again')
                  print('You have ' +str(int(self.attempts))+ ' attempts before lock-out')
              elif self.attempts == 1:
                  self.keypad_array.clear()
                  print('Try Again')
                  print('You have ' +str(int(self.attempts))+ ' attempt before lock-out')
              else:
                  self.keypad_array.clear()
                  print('You have been locked out!')
                  

#Main Program

keypad=Keypad()

keypad.define_master_password()

while keypad.attempts > 0:
    
    keypad.enter_password()
    keypad.verify_password()
    
    if keypad.attempts == 0 or keypad.reset_attempts == 0:
        break