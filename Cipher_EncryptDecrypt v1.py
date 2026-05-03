def run_cipher(choice):
   match choice:
        case 1:
            print('Encrytion')
            try:
                shift=int(input('Enter Shift Value:'))
            except ValueError:
                print("Error: Please enter a valid integer.")
                return
            plain_string=input('Enter the string: ')
        case 2:
           pass
            
        




while True:
    print('Enter 1 for Encryption')
    print('Enter 2 for Decryption')
    print('Enter 3 to Quit')
    try:
        choice=int(input('\nEnter your choice:'))
    except ValueError:
        print("Error: Please enter a valid integer.\n")
        continue
    match choice:
        case 1:
            run_cipher(choice)
        case 2:
            run_cipher(choice)
        case 3:
            print('Exiting')
            break
        case _:
            print('Enter a Valid Option\n')
            