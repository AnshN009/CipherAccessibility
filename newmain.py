import random
import math
#Add a clause that prevents the code from crashing
#By checking if a string ever has a non-letter character
#By seeing if it has checked through all possible characters, in alphadict without finding a match
#If so, say that the string cannot be encrypted or decrypted
#All other codes I can add in the future: Aristocrat K2, Aristocrat K3, Aristocrat K4, Patristocrat, Morbit, Running Key, Railfence, Hill Cipher, etc...
wrong = "abcdefghijlklmnopqrstuvwxyz!@#$%^&*()<>?:{}|_+~`-=[]\;',./"
print("The Cipher-tron 3000")
morselib = {0: ".-x", 1: "-...x", 2: "-.-.x", 3: "-..x", 4: ".x", 5: "..-.x", 6: "--.x", 7: "....x", 8: "..x", 9: ".---x", 10: "-.-x", 11: ".-..x", 12: "--x", 13: "-.x", 14: "---x", 15: ".--.x", 16: "--.-x", 17: ".-.x", 18: "...x", 19: "-x", 20: "..-x", 21: "...-x", 22: ".--x", 23: "-..-x", 24: "-.--x", 25: "--..x"}
alphadict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}
portatab = {0: "nopqrstuvwxyzabcdefghijklm"}
typeofmach = ""
key = "" 

print("Setting up machine...Please Wait...")
for i in range(random.randint(1,7)):
    print("...")

def corrector(secret):
    #Take out any non-letter characters in the key
    output = ""
    for i in secret:
        checker = 0
        while alphadict[checker] != i and checker < 25:
            checker += 1
        if checker >= 25:
            print("The secret phrase contains a character")
            print("That cannot be processed(a space, number, special character, etc.)")
            boolean = input("Would you like to remove " + i + "? Say Y if yes, N if no. ")
            if boolean != "Y":
                reuse()
        else:
            output += i
    return output
                
def vencryptor(ekey):
    secret = input("What is the secret message?: ")
    secret = corrector(secret)
    print("Secret Phrase: " + secret)
    ciphered = ""
    character = 0 
    while character < len(secret):
        letterofsec = 0
        letterofkey = 0
        cycleofkey = 0
        while secret[character] != alphadict[letterofsec]:
            letterofsec += 1
        #Finds what letter the character'th letter of the secret message is
        cycleofkey = character % len(ekey)
        '''
        If the key is shorter than the secret, line above
        uses the first letter of the key after the last letter 
        was used, restarting the cycle
        '''
        while ekey[cycleofkey] != alphadict[letterofkey]:
            letterofkey += 1
        #Finds what letter the character'th letter of the key is
        sumofboth = (letterofsec + letterofkey) % 26
        #Adds the two letters together, with a modulus
        ciphered += alphadict[sumofboth]
        character += 1
    print("'" + ciphered + "'")

def vdecryptor(dkey):
    weird = input("Please enter the passing phrase(No spaces or special characters): ")
    weird = corrector(weird)
    print("Passing Phrase: " + weird)
    deciphered = ""
    dcharacter = 0 
    while dcharacter < len(weird):
        letterofp = 0
        dletterofkey = 0
        while weird[dcharacter] != alphadict[letterofp]:
            letterofp += 1
        dcycleofkey = dcharacter % len(dkey)
        while dkey[dcycleofkey] != alphadict[dletterofkey]:
            dletterofkey += 1
        dletterofboth = (letterofp - dletterofkey) % 26
        deciphered += alphadict[dletterofboth]  
        dcharacter += 1
    print("'" + deciphered + "'")

def help_function():
    print("")
    print("CIPHER-TRON 3000 INFO")
    print("")
    print("The Cipher-tron 3000 was built by Ansh N.")
    print("It is currently in development, but")
    print("we plan to eventually have as many as possible.")
    print("There are 8 codes in development right now,")
    print("but we cannot presume any information, and need")
    print("the user to input all of the information(i.e. code word, key, etc.)")
    print("Furthermore, we cannot have any non-letter characters.")
    print("This would crash the program, and even if it was possible")
    print("It would greatly damage the security of the program.")
    print("")
    print("The following codes are:")
    print("Vigenere - Encryption with a code word; call with /Vigenere")
    print("Caesar - Encryption with a number shift; call with /Caesar")
    print("Atbash - Encryption with a reversed alphabet; call with /Atbash")
    print("Aristocrat - Encryption with an alphabet replacement; call with /AristK1")
    print("Baconian - Encryption with a binary transformation; call with /Baconian")
    print("Pollux - Encryption with morse code and random numbers; call with /Pollux")
    print("Affine - Encryption with a mathematical transformation; call with /Affine")
    print("Porta - Encryption with a porta table and key; call with /Porta")
    print("Morse - Encryption with dots, dashes, and x's; call with /Morse")
    print("Type in /exit to leave a machine")

def vigenere():
    print("Vigenere Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Vigenere Cipher Encryptor")
        key = input("Please enter the key word for today: ")
        key = corrector(key)
        print("Key: " + key)
        vencryptor(key)
    elif typeofmach == "D":
        print ("Vigenere Cipher Decryptor")
        key = input("Please enter the key word for today: ")
        key = corrector(key)
        print("Key: " + key)
        vdecryptor(key)
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        vigenere()

def caesar():
    # CREATE A CLAUSE TO PREVENT THE KEY FROM NOT BEING A NUMBER
    # Literally just a vigenere with a one-letter key
    print("Caesar Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Caesar Cipher Encryptor")
        key = input("Please enter the shift as a two-digit number between 0-25 for today: ")
        output = ""
        for i in key:
            checker = 0
            while i != wrong[checker] and checker < len(wrong) - 1:
                checker += 1
            if checker <= len(wrong):
                print("The secret phrase contains a character")
                print("That cannot be processed.")
                print("(a space, letter, special character, etc.")
                print("Would you like to remove '" + i + "'?")
                boolean = input("Say Y if yes, N if no. ")
                if boolean == "Y":
                    print("Character might lead to a crash.")
                    boolean = input("If this is not wanted, type in /exit")
                    if boolean == "/exit":
                        caesar()
                    else: 
                        output += key
                else: 
                    print("Character removed.")
            else:
                output += i
            key = output
        if output == "":
            print("Key did not contain a number")
            reuse()
        print("Shift: " + key)
        vencryptor(alphadict[int(key) % 26])
    elif typeofmach == "D":
        print ("Caesar Cipher Decryptor")
        key = input("Please enter the shift for today: ")
        output = ""
        output = ""
        for i in key:
            checker = 0
            while i != wrong[checker] and checker < len(wrong) - 1:
                checker += 1
            if checker <= len(wrong):
                print("The secret phrase contains a character")
                print("That cannot be processed.")
                print("(a space, letter, special character, etc.")
                print("Would you like to remove '" + i + "'?")
                boolean = input("Say Y if yes, N if no. ")
                if boolean == "Y":
                    print("Character might lead to a crash.")
                    boolean = input("If this is not wanted, type in /exit")
                    if boolean == "/exit":
                        caesar()
                    else: 
                        output += key
                else: 
                    print("Character removed.")
            else:
                output += i
            key = output
        if output == "":
            print("Key did not contain a number")
            reuse()
        print("Shift: " + key)
        
        vdecryptor(alphadict[int(key) % 26])
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        caesar()

def atbash():
    # Could be done with erist function, but that's not necessary
    print("Atbash Cipher Machine")
    typeofmach = input("Type E or D to access the machine: ") 
    if (typeofmach == "E") or (typeofmach == "D"):
        print ("Atbash Cipher Encryptor & Decryptor")
        phrase = input("Please enter the phrase(No spaces or special characters): ")
        phrase = corrector(phrase)
        print("Phrase: " + phrase)
        deciphered = ""
        for acharacter in phrase:
            whatchar = 0
            while (alphadict[whatchar] != acharacter):
                whatchar += 1
            deciphered += alphadict[25 - whatchar]
        print("'" + deciphered + "'")
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        atbash()

def econian():
    message = input("What is the secret phrase?: ")
    message = corrector(message)
    output = ""
    for i in message:
        match = 0
        while alphadict[match] != i:
            match += 1
        #It would be far shorter to use a binary library, but i didn't want to write that out - binlibr = {0: "AAAAA", 1: "AAAAB", 2: "AAABA", 3: "AAABB", 4: "AABAA", 5: "AABAB"...}
        if match >= 16:
            output += "B"
            match -= 16
        else:
            output += "A"
        if match >= 8:
            output += "B"
            match -= 8
        else:
            output += "A"
        if match >= 4:
            output += "B"
            match -= 4
        else:
            output += "A"
        if match >= 2:
            output += "B"
            match -= 2
        else:
            output += "A"
        if match >= 1:
            output += "B"
            match -= 1
        else:
            output += "A"
    print(output)

def deconian():
    passing = input("What is the passing phrase?: ")
    charanum = 0
    output = ""
    while charanum < len(passing):
        num = 0
        if passing[charanum] == "B":
            num += 16
        elif passing[charanum] != "A":
            print("Passing phrase is unsatisfactory.")
            baconian()
        if passing[charanum + 1] == "B":
            num += 8
        elif passing[charanum + 1] != "A":
            print("Passing phrase is unsatisfactory.")
            baconian()
        if passing[charanum + 2] == "B":
            num += 4
        elif passing[charanum + 2] != "A":
            print("Passing phrase is unsatisfactory.")
            baconian()    
        if passing[charanum + 3] == "B":
            num += 2
        elif passing[charanum + 3] != "A":
            print("Passing phrase is unsatisfactory.")
            baconian()
        if passing[charanum + 4] == "B":
            num += 1
        elif passing[charanum] != "A":
            print("Passing phrase is unsatisfactory.")
            baconian()
        output += alphadict[num]
        charanum += 5
    print(output)    
    
def baconian():
    print("Baconian Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Baconian Cipher Encryptor")
        econian()
    elif typeofmach == "D":
        print ("Baconian Cipher Decryptor")
        deconian()
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        baconian()

def emorse(message):
    interm = ""
    output = ""
    for character in message:
        match = 0
        while alphadict[match] != character:
            match += 1
        interm += morselib[match]
    return(interm)

def demorse(message):    
    charamorse = 0
    output = ""
    while charamorse < len(message):
        match = 0
        fullcharamorse = ""
        while message[charamorse] != "x":
            fullcharamorse += message[charamorse]
            charamorse += 1
        charamorse += 1
        fullcharamorse += "x"
        while morselib[match] != fullcharamorse:
            match += 1
        output += alphadict[match]
    return output

def ellux(morsestr):
    print("Only input numbers between 0-9 inclusive, no commas necessary.")
    print("Typing non-integer characters will crash machine.")
    dots = input("Which numbers would represent dots?: ")
    dots = str(int(dots))
    lines = input("Which numbers would represent lines?: ")
    lines = str(int(lines))
    spaces = input("Which numbers would represent spaces?: ")
    spaces = str(int(spaces))
    character = 0
    output = ""
    choice = 0
    while character < len(morsestr):
        if morsestr[character] == ".":
            choice = random.randint(0, len(dots) - 1)
            output += dots[choice]
        if morsestr[character] == "-":
            choice = random.randint(0, len(lines) - 1)
            output += lines[choice]
        if morsestr[character] == "x":
            choice = random.randint(0, len(spaces) - 1)
            output += spaces[choice]
        character += 1
    print(output)

def dellux(numstring):
    print("Only input numbers between 0-9 inclusive, no commas necessary.")
    print("Typing non-integer characters will crash machine.")
    dots = input("Which numbers represent dots?: ")
    dots = str(int(dots))
    lines = input("Which numbers represent lines?: ")
    lines = str(int(lines))
    spaces = input("Which numbers represent spaces?: ")
    spaces = str(int(spaces))
    character = 0
    interm = ""
    while character < len(numstring):
        for num in dots:
            if numstring[character] == num:
                interm += "."
        for num in lines:
            if numstring[character] == num:
                interm += "-"
        for num in spaces: 
            if numstring[character] == num:
                interm += "x"
        character += 1
    print(demorse(interm))

def pollux():
    print("Pollux Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Pollux Cipher Encryptor")
        message = input("What is the secret phrase?: ")
        message = corrector(message)
        ellux(emorse(message))
    elif typeofmach == "D":
        print ("Pollux Cipher Decryptor")
        message = input("What is the passing phrase?: ")
        message = corrector(message)
        dellux(message)
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        pollux()

def morse():
    print("Morse Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Morse Cipher Encryptor")
        message = input("What is the secret message?: ")
        message = corrector(message)
        print(emorse(message))
    elif typeofmach == "D":
        print ("Morse Cipher Decryptor")
        message = input("What is the passing phrase?: ")
        message = corrector(message)
        print(demorse(message))
    elif typeofmach == "/exit":
        reuse()
    else:
        print("Please choose a machine")
        morse()

def effine():
    coef = int(input("Please enter the coefficient for today: "))
    print("Coefficient: " + str(coef))
    const = int(input("Please enter the constant for today: "))
    print("Constant: " + str(const))
    message = input("Please enter the message for today: ")
    print("Message: " + message)
    message = corrector(message)
    charanum = 0
    output = ""
    while charanum < len(message):
        match = 0
        while message[charanum] != alphadict[match]:
            match += 1
        output += alphadict[((match * coef) + const) % 26]
        charanum += 1
    print(output)

def dffine():
    print("Coefficient and Constant Formula must make distinct outputs for each letter.")
    coef = int(input("Please enter the coefficient for today: "))
    print("Coefficient: " + str(coef))
    const = int(input("Please enter the constant for today: "))
    print("Constant: " + str(const))
    message = input("Please enter the passer for today: ")
    message = corrector(message)
    print("Passer: " + message)
    charanum = 0
    real = ""
    while charanum < len(message):
        match = 0
        while message[charanum] != alphadict[match]:
            match += 1
        match = match - const
        while (match / coef) != math.floor(match / coef):
            match += 26
        real += alphadict[(match / coef) % 26]
        charanum += 1
    print(real)

def affine():
    print("Affine Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Affine Cipher Encryptor")
        effine()

    elif typeofmach == "D":
        print ("Affine Cipher Decryptor")
        dffine()

    elif typeofmach == "/exit":
        reuse()

    else:
        print("Please choose a machine")
        affine()
        
def porter():
    #Makes the porta table
    #I could've made a dictionary but that's tiring
    for i in range(12):
        p1string = "nopqrstuvwxyz"
        p2string = "abcdefghijklm"
        counter = 0
        newstring = ""
        #Adapts p1
        while counter < (12 - i):
            newstring += p1string[counter + i]
            counter += 1
        counter = 0
        while counter < i:
            newstring += p1string[counter]
            counter += 1
        counter = 0
        #Adapts p2
        while counter < i + 1:
            newstring += p2string[(12 - i) + counter]
            counter += 1
        counter = 0
        while len(newstring) < 25:
            newstring += p2string[counter]
            counter += 1
        portatab[i] = newstring

porter()   

def eorta():
    message = input("What is the secret phrase?: ")
    message = corrector(message)
    print("Message: " + message)
    key = input("What is the key word: ")
    key = corrector(key)
    print("Key: " + key)
    keystr = ""
    output = ""
    character = 0 
    for i in message:
        keystr += key[character % len(key)]
        character += 1
    character = 0
    for i in keystr:
        counter = 0
        while alphadict[counter] != i:
            counter += 1
        counter = math.floor(counter / 2)
        counter2 = 0
        while alphadict[counter2] != message[character]:
            counter2 += 1
        output += portatab[counter][counter2]
        character += 1
    print(output)   

def deorta():
    message = input("What is the passing phrase?: ")
    message = corrector(message)
    print("Passing: " + message)
    key = input("What is the key word: ")
    key = corrector(key)
    print("Key: " + key)
    keystr = ""
    output = ""
    character = 0 
    for i in message:
        keystr += key[character % len(key)]
        character += 1
    character = 0
    for i in keystr:
        counter = 0
        while alphadict[counter] != i:
            counter += 1
        counter = math.floor(counter / 2)
        counter2 = 0
        while portatab[counter][counter2] != message[character]:
            counter2 += 1
        output += alphadict[counter2]
        character += 1
    print(output)

def porta():
    #Perhaps create a dictionary, with each pair in the 1st column and their corresponding row of letters in the actual porta table
    print("Porta Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Porta Cipher Encryptor")
        eorta()

    elif typeofmach == "D":
        print ("Porta Cipher Decryptor")
        deorta()

    elif typeofmach == "/exit":
        reuse()

    else:
        print("Please choose a machine")
        porta()

def erist():
    message = input("What is the secret phrase?: ")
    message = corrector(message)
    print("To enter the key correctly, enter the letter that corresponds to a, then b...")
    print("Keep doing so until the key is 26 letters.")
    print("Machine will interpret this as the first letter of input is a, second is b...")
    print("Reusing letters means that decryption will likely not be correct")
    key = input("What is the key?: ")
    if len(key) != 26:
        print("The Key is not long enough.")
        aristocratk1()
    key = corrector(key)
    output = ""
    for character in message:
        match = 0
        while alphadict[match] != character:
            match += 1
        output += key[match]
    print(output)

def derist():
    message = input("What is the passing phrase?: ")
    message = corrector(message)
    print("To enter the key correctly, enter the letter that corresponds to a, then b...")
    print("Keep doing so until the key is 26 letters.")
    print("Machine will interpret this as the first letter of input is a, second is b...")
    print("Reusing letters means that decryption will likely not be correct")
    key = input("What is the key?: ")
    if len(key) != 26:
        print("The Key is not long enough.")
        aristocratk1()
    key = corrector(key)
    output = ""
    for character in message:
        match = 0
        while key[match] != character:
            match += 1
        output += alphadict[match]
    print(output)

def aristocratk1():
    print("Aristocrat K1 Cipher Machine")
    typeofmach = input("Type E for the Encryptor or type D for the decryptor: ") 
    if typeofmach == "E":
        print ("Aristocrat K1 Cipher Encryptor")
        erist()

    elif typeofmach == "D":
        print ("Aristocrat K1 Cipher Decryptor")
        derist()

    elif typeofmach == "/exit":
        reuse()

    else:
        print("Please choose a machine")
        aristocratk1()

def reuse():
    #Add a clause that extends the commands to be /[full name], ex: /vignere, /caesar
    typeofmach = input("Type /help for info, or call on a cipher: ") 
    if typeofmach == "/help":
        help_function()
    elif typeofmach == "/Vigenere":
        vigenere()
    elif typeofmach == "/Caesar":
        caesar()
    elif typeofmach == "/Atbash":
        atbash()
    elif typeofmach == "/AristK1":
        aristocratk1()
    elif typeofmach == "/Baconian":
        baconian()
    elif typeofmach == "/Pollux":
        pollux()
    elif typeofmach == "/Affine":
        affine()
    elif typeofmach == "/Porta":
        porta()
    elif typeofmach == "/Morse":
        morse()
    elif typeofmach == "/exit":
        print("")
        print("Inititating Crashout/Exit Sequence...")
        for i in range(random.randint(2,9)):
            print("...")
        print("Thank you for using the Cipher-Tron 3000!")
        print(alphadict["Goodbye!"])
    else:
        print("Please choose a machine")
    reuse()       
reuse()
