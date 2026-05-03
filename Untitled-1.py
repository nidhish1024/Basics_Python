def encrypt(plain_string,shift):
    encrypted_string=''
    for i in plain_string:
        if i.isalpha():
            if i.isupper():
                base=ord('A')
                encrypted_string+=chr((ord(i)-base+shift)%26+base)

            elif i.islower():
                base=ord('a')
                encrypted_string+=chr((ord(i)-base+shift)%26+base)

        else:
            encrypted_string+=i
            
    return encrypted_string

def selection():
    print('''Enter 1 to Encrypt the string''')
    print('''Enter 2 to Decrypt the string''')
    option = int(input('Enter the Option:'))
    return option

def run_cipher(n):
    if n==1:
        print("Encrypt Mode")
        shift=int(input('Enter the shifting cipher:'))
        user_str=input("Enter the string to be encrypted:")
        some_str=encrypt(user_str,shift)
        print(some_str)
    elif n==2:
        print("Decrypt Mode")
        shift=(int(input('Enter the shifting cipher:')))
        user_str=input("Enter the string to be decrypted:")
        some_str=encrypt(user_str,-shift)
        print(some_str)
    else:
        print("Enter A Valid option!")

n=selection()
run_cipher(n)