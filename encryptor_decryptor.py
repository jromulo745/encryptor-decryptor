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

def decryptor(string):
    decrypted_string = ""
    string_list = []
    counter_1 = 0
    counter_2 = -1
    string_mirror = string
    
    for x in range(len(string_mirror)):
        string_list.append("")
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    while (len(string_mirror) != 0):
        if (len(string_mirror) != 1):
            string_list[counter_1] = string_mirror[0]
            string_list[counter_2] = string_mirror[1]
            string_mirror = string_mirror[2:]
            counter_1 += 1
            counter_2 -= 1
        else:
            string_list[int(len(string) / 2)] = string_mirror
            string_mirror = ""
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    for letter in string_list:
        decrypted_string += letter
        
    return decrypted_string

#---------------------------------------------------------------------------------------

os.system("clear")

# main section
program_runs = True

while (program_runs == True):
    print()
    print("\t1 - Encryptor")
    print("\t2 - Decryptor")
    print("\t3 - Quit")
    user_input = int(input("\n\tSelect a choice (1 - 3): "))
    os.system("clear")
    if (user_input == 1): # encrypt
        password = str(input("\n\tEnter a password to encrypt: "))
        string = encryptor(password)
        print("\n\tHere is your encrypted password: " + string)
        wait_input = str(input("\n\tHit enter to continue..."))
        os.system("clear")
    elif (user_input == 2):
        password = str(input("\n\tEnter encrypted password: "))
        string = decryptor(password)
        os.system("clear")
        print("\n\tHere is your decrypted password: " + string)
        wait_input = str(input("\n\tHit enter to continue..."))
        os.system("clear")
    elif (user_input == 3): # quit
        program_runs = False
    else:
        print(" --------------- ")
        print("| Invalid Input |")
        print(" ---------------")
