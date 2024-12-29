import math
portatab = {0: "nopqrstuvwxyzabcdefghijklm"}
alphadict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}

def porter():
    #Makes the porta table
    for i in range(12):
        p1string = "nopqrstuvwxyz"
        p2string = "abcdefghijklm"
        counter = 0
        newstring = ""
        # First part from p1string
        while counter < (12 - i):
            newstring += p1string[counter + i]
            counter += 1
        # Reset counter before next section
        counter = 0
        while counter < i:
            newstring += p1string[counter]
            counter += 1
        counter = 0
        # Add characters from p2string
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
    print("Message: " + message)
    key = input("What is the key word: ")
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
eorta()