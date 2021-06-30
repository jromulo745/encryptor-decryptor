#

'''
encryptor_decryptor_program
(designed for Terminal (macOS) console output)
'''

#---------------------------------------------------------------------------------------

import os

#---------------------------------------------------------------------------------------

# encryptor function
def encryptor(string):
    encrypted_string = ""
    string_mirror = string
    
    while ((len(string_mirror)) != 1) and (len(string_mirror) != 2):
        encrypted_string += string_mirror[0]
        encrypted_string += string_mirror[-1]
        string_mirror = string_mirror[1:-1]
        
    encrypted_string += string_mirror
    return encrypted_string
    
    
#---------------------------------------------------------------------------------------

# main section
program_runs = True

while (program_runs == True):
    print()
    print("\t1 - Encryptor")
    print("\t2 - Quit")
    user_input = int(input("\n\tSelect a choice (1 - 2): "))
    os.system("clear")
    if (user_input == 1): # encrypt
        password = str(input("\n\tEnter a password to encrypt: "))
        string = encryptor(password)
        print("\n\tHere is your encrypted password: " + string)
        wait_input = str(input("\n\tHit enter to continue..."))
        os.system("clear")
    elif (user_input == 2): # quit
        program_runs = False
    else:
        print(" --------------- ")
        print("| Invalid Input |")
        print(" ---------------")
    

    


