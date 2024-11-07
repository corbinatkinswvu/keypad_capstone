#Example for Keypad Password Inputting

master_password_array=list()
print('Set 6-digit Password:')
for index in range(6):
    master_number=int(input())
    master_password_array.append(master_number)


keypad_button_array=list()
print('Enter 6-Digit Password:')
for index in range(6):
    keypad_number=int(input())
    keypad_button_array.append(keypad_number)
    

if keypad_button_array == master_password_array:
    print('Success!')
    
elif keypad_button_array == [0,0,0,0,0,0]:
    print('Enter Current Password:')   
    while keypad_button_array == [0,0,0,0,0,0]:
        for index in range(6):
            keypad_button_array.remove(0)
        for index in range(6):
            master_number=int(input())
            master_password_array.append(keypad_number)

print('Password is ' +str(keypad_button_array)+ ' ')
