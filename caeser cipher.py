#Enhanced Version of Caeser Cipher Encryption/Decryption Algorithm with "random shift values"

import random as rand   # importing Random module

def encrypt(nortxt):    # creating Encryption Function

    entxt = ""  # empty string
    shift_list = []     # empty list

    # iterating through the given string
    for i in nortxt:

        # using random module to generate random shift values
        shift = rand.randint(0, 9)
        shift_list.append(str(shift))

        if int(shift)%2 == 0:   # shift values based on odd or even number
            shiftxtnum = ord(i) + shift # if it is even the value is shifted to right i.e added
        else:
            shiftxtnum = ord(i) - shift # if it is odd the value is shifted to left i.e subtracted

        shiftxt = chr(shiftxtnum)
        entxt += shiftxt    # encrypted string is concatinated
    
    return entxt, ''.join(shift_list)   # returning encrypted text and encryption key



def decrypt(entxt, shift_list): # creating decryption fucntion

    newlist = []    # empty List
    detxt = ""  # empty string

    for i in shift_list:    # removing any unwanted characters in the key
        if i not in (" ", "[", "]", ","):
            newlist.append(int(i))

    lstindex = 0
    # iterating through the encrypted text to decrypt it
    for i in entxt:
        sft = newlist[lstindex] # location of the list at given postion 

        if sft%2 == 0:  # shift values based on odd or even number
            shiftxtnum = ord(i) - sft   # if it is even the value is shifted to left i.e subtracted
        else:
            shiftxtnum = ord(i) + sft   # if it is odd the value is shifted to right i.e added
        shiftxt = chr(shiftxtnum)
        detxt += shiftxt
        lstindex += 1
    
    return detxt



print()

# input string
text1 = str(input("Enter String: "))

print()

# encrypting text using encrypt fucntion
encrypt_result, key = encrypt(text1)    
print("Encrypted text:", encrypt_result)

# enryption key
print("Key:", key) 
print()

# taking encrypted string
text2 = str(input("Enter Encrypted String: "))
print()

# inputting key to use decryption
key2 = input("Enter the Key: ")
print()

decrypt_result = decrypt(text2, key2)

# decrypted text(should be same as input string)
print("Decrypted Result:", decrypt_result)
