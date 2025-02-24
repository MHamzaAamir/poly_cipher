import random
import sys

keymap = "abcdefghijklmnopqrstuvwxyz "
pol1 = []
pol2 = []
pol3 = []

def string_to_list(string_input):
    elements = string_input.strip('[]').split(',')
    float_list = [float(elem.strip()) for elem in elements]
    return float_list

print("""Poly Cipher
      
Select One Option: 
1) Auto Key Generation
2) Manual Key Input""")

choice = int(input())

if (choice == 1):
    for i in range(6):
        if (i == 0 or i == 1):
            pol1 = pol1 + [round(random.uniform(1, 100),8)]
        elif (i == 2 or i == 3):
            pol2 = pol2 + [round(random.uniform(1, 100),8)]
        elif (i == 4 or i == 5):
            pol3 = pol3 + [round(random.uniform(1, 100),8)]
elif (choice == 2):
    print("Enter Key")
    x = input()
    key = string_to_list(x)
    pol1 = [key[0],key[1]]
    pol2 = [key[2],key[3]]
    pol3 = [key[4],key[5]]
else:
    print("Error!!")
    sys.exit()

key = [pol1[0],pol1[1],pol2[0],pol2[1],pol3[0],pol3[1]]

plaintext = input("Enter Plain Text: ")
plaintext = plaintext.lower()
length = len(plaintext)
count = 0
ciphertext = ""
for i in range(length):
    x = keymap.find(plaintext[i])
    y = 0
    if (count == 0):
        y = pol1[0]*(x**2)+pol1[1]
        count += 1
    elif (count == 1):
        y = pol2[0]*(x**2)+pol2[1]
        count += 1
    elif (count == 2):
        y = pol3[0]*(x**2)+pol3[1]
        count = 0

    y = str(round(y, 4))
    substr = ""
    for i in y:
        if(i.isdigit()):
            if len(substr) == 0:
                substr += i
            elif len(substr) == 1:
                substr += i
                number = int(substr)
                if 10 <= number <= 25:
                    ciphertext += keymap[number]
                    substr = ""
                else:
                    digit1 = number // 10
                    digit2 = number % 10
                    ciphertext += keymap[digit1]
                    ciphertext += keymap[digit2]
                    substr = ""
        elif (i=="."):
            if len(substr) == 1:
                number = int(substr)
                ciphertext += keymap[number]
            ciphertext += i
            substr = ""

    a = random.randint(1,9)
    if (a == 1):
        ciphertext = ciphertext + "/"
    elif(a==2):
        ciphertext = ciphertext + "@"   
    elif (a==3):
        ciphertext = ciphertext + "|"
    elif(a==4):
        ciphertext = ciphertext + "&"
    elif(a==5):
        ciphertext = ciphertext + "#"
    elif(a==6):
        ciphertext = ciphertext + ")"
    elif(a==7):
        ciphertext = ciphertext + "("
    elif(a==8):
        ciphertext = ciphertext + "!"
    elif(a==9):
        ciphertext = ciphertext + "^"

print("")
print("Ciphertext: ",ciphertext)
print("")
print("Key: ",key)