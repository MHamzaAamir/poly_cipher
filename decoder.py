import math

keymap = "abcdefghijklmnopqrstuvwxyz "


def string_to_list(string_input):
    elements = string_input.strip('[]').split(',')
    float_list = [float(elem.strip()) for elem in elements]
    return float_list


print("Enter Key")
x = input()
key = string_to_list(x)
pol1 = [key[0],key[1]]
pol2 = [key[2],key[3]]
pol3 = [key[4],key[5]]



print("Enter Ciphertext:")
ciphertext = input()
decipher = ""
count = 0
plaintext = ""
for i in ciphertext:
    if(i == "."):
        decipher += i
    elif(i.isalpha()):
        decipher += str(keymap.find(i))
    else:
        x = float(decipher)
        if count == 0:
            g = (x-pol1[1])/pol1[0]
            if g<0:
                g = 0
            d = math.sqrt(g)
            y = round(d)
            count += 1
        elif count == 1:
            g = (x-pol2[1])/pol2[0]
            if g<0:
                g = 0
            d = math.sqrt(g)
            y = round(d)
            count += 1
        elif count == 2:
            g = (x-pol3[1])/pol3[0]
            if g<0:
                g = 0
            d = math.sqrt(g)
            y = round(d)
            count = 0
        decipher = ""
        plaintext += keymap[y]
    

print("")

print("Plaintext:",plaintext)
