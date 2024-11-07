#This is the first iteration of the barcode scanner code
#Tracking number is made of letters and numbers. How will this work for the keypad?
#It appears that tracking numbers are 16 characters in length
#It appears that a entering the tracking number on the homeowner's keypad is unviable. Could have a fixed tracking number for demonstration purposes (future work)

#Notes:
#int may have to be added to append(int(number)) in the future if letters are not taken in array
#range is a built-in function that increments the counter for the programmer


#Code to install necessary python libraries
#pip install pyzbar
#pip install opencv-python

#Code to import necessary python libraries
import pyzbar
import cv2

#Defining the initial variables for the barcode scanner

class BarcodeScanner:

    def __init__(self):
        self.scanned_barcode=[]
        self.alarm_counter=3
        self.scanned_image=None
        self.detected_barcode=[]
        self.starting_point=(1,1)
        self.ending_point=(225,225)
        self.color=(0,0,0)
        self.thickness=2
    
    def input_tracking_number(self):
        self.inputted_tracking_number_array=list()
        self.tracking_number_elements=input('Enter the total length of the tracking number:')
        print('Enter your tracking number here!')
        for index in range(int(self.tracking_number_elements)):
            self.number=input('Number:')
            self.inputted_tracking_number_array.append((number))
    
 
    def barcode_scanner(self):
        self.image=cv2.imread(self.scanned_image)
        self.detected_barcode=decode(self.image)
        if not self.detected_barcode:
            print('Placeholder')
        else:
            self.image=cv2.rect(self.image,self.starting_point,self.ending_point,self.color,self.thickness)
            
        #Display image on toolbar
        cv2.imshow("Image",self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def barcode_compare(self):
        if self.inputted_tracking_number_array == self.detected_barcode:
            self.alarm_counter=3
            #Send high signal to solenoid
        else:
            self.alarm_counter=self.alarm_counter-1
            if self.alarm_counter == 2:
                print('Try Again!')
                print('You have ' +str(int(self.alarm_counter))+ ' attempts left before being locked out!')
            elif self.alarm_counter == 1:
                print('Try Again!')
                print('You have ' +str(int(self.alarm_counter))+ ' attempt left before being locked out!')
            elif self.alarm_counter == 0:
                print('Locked Out!')
            else:
                print('Error!')


#Main Program/Loop

scanner=BarcodeScanner()

while scanner.alarm_counter > 0:
    
    scanner.input_tracking_number()
    scanner.barcode_scanner()
    scanner.barcode_compare()
    
    if scanner.alarm_counter == 0:
        break
    
