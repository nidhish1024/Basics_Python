
def encryption(plain_string,shift):
    encrypted_string=''
    for char in plain_string:
        if char.isalpha():
            if char.isupper():
                    base=ord('A')
                    encrypted_string+=chr((ord(char)-base+shift)%26+base)
            elif char.islower():
                    base=ord('a')
                    encrypted_string+=chr((ord(char)-base+shift)%26+base)
        else:
            encrypted_string+=char
    return encrypted_string

def brute_force_decryption(encrypted_string):
    for shift in range(26):
        print(f'Shift: {shift} Decrypted String: {encryption(encrypted_string,-shift)}')
         
def run_cipher(choice):

   match choice:
        case 1:
            print('\nEncryption')
            try:
                shift=int(input('\nEnter Shift Value:'))
            except ValueError:
                print("Error: Please enter a valid integer.")
                return
            plain_string=input('Enter the string: ')
            print('Encrypted String:',encryption(plain_string,shift),'\n')
        case 2:
            print('\nDecryption')
            try:
                shift=int(input('\nEnter Shift Value:'))
            except ValueError:
                print("Error: Please enter a valid integer.")
                return
            plain_string=input('Enter the string: ')
            print('Decrypted String:',encryption(plain_string,-shift),'\n') 
        case 3:
            print('\nBrute Force Decryption')
            encrypted_string=input('Enter the string: ')
            brute_force_decryption(encrypted_string)           
            
while True:
    print('Enter 1 for Encryption')
    print('Enter 2 for Decryption')
    print('Enter 3 for Brute Force Decryption')
    print('Enter 4 to Quit')
    try:
        choice=int(input('\nEnter your choice:'))
    except ValueError:
        print("Error: Please enter a valid integer.\n")
        continue
    match choice:
        case 1|2|3:
            run_cipher(choice)
        case 4:
            print('Exiting')
            break
        case _:
            print('Enter a Valid Option\n')
            
