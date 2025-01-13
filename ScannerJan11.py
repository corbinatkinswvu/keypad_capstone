#1/11/25 Update for Barcode Scanner

import pyzbar
import cv2

class Scanner:
    
    def __init__(self):
        
        self.alarm_counter=3
        
        self.scanned_image=None
        
        self.detected_barcode=[]
        
        self.starting_point=(1,1)
        
        self.ending_point=(225,225)
        
        self.color=(0,0,0)
        
        slef.thickness=2
        
        
    def barcode_select(self):
        print('Press 0 for Long Barcodes.')
        print(' ')
        print('Press 1 for Short Barcodes.')
        print(' ')
        print('Press 2 for Special Barcodes.')
        
        self.barcode_option=int(input())
        
        if self.barcode_option == 0:
            print('Input Long Barcode:')
            self.tracking_number_array.append('1')
            self.tracking_number_array.append('Z')
            for index in range(16):
                self.tracking_number_input=input()
                self.tracking_number_array.append(self.tracking_number_input)
                
            print(self.tracking_number_array)
            
        elif self.barcode_option == 1:
            print('Input Short Barcode:')
            for index in range(11):
                self.tracking_number_input=input()
                self.tracking_number_array.append(self.tracking_number_input)
                
            print(self.tracking_number_array)
        
        elif self.barcode_option == 2:
            print('Input Special Barcode:')
            self.tracking_number_array.append('T')
            for index in range(10):
                self.tracking_number_input=input()
                self.tracking_number_array.append(self.tracking_number_input)
                
            print(self.tracking_number_array)
            
        else:
            print('Invalid Input! Please Try Again!')
            
    def barcode_scan(self):
        
        self.image=cv2.imread(self.scanned_image)
        
        self.detected_barcode=decode(self.image)
        
        if not self.detected_barcode:
            print('Placeholder')
            
        else:
            self.image=cv2.rect(self.image,self.starting_point,self.ending_point,self.color,self.thickness)
            
        cv2.imshow("Image",self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def barcode_compare(self):
        
        if self.tracking_number_array == self.detected_barcode:
            self.alarm_counter=3
            print('Success!')
            
        else:
            self.alarm_counter=self.alarm_counter-1
            
            if self.alarm_counter == 2:
                print('Try Again!')
                print('You have ' +str(int(self.alarm_counter))+ ' attempts left!')
                
            elif self.alarm_counter == 1:
                print('Try Again!')
                print('You have ' +str(int(self.alarm_counter))+ ' attempt left!')
                
            elif self.alarm_counter == 0:
                print('Locked Out!')
                
            else:
                print('Error')
                

barcode_scanner=Scanner()

while scanner.alarm_counter > 0:
    
    barcode_scanner.barcode_select()
    barcode_scanner.barcode_scan()
    barcode_scanner.barcode_compare()
    
    if barcode_scanner.alarm_counter == 0:
        break
    