hex = "011b"
hex1 = hex[0:2]
hex2 = hex[2:4]
dec1 = int(hex1, 16)
dec2 = int(hex2, 16)
deccom = int(hex, 16)

bc = bin(int(hex, 16))[2:]

b1 = bin(dec1)[2:]
b2 = bin(dec2)[2:]

p = 0
l1 = [*b1]
bl = [*bc]

for i in range(len(bc)):
    try:
        if i == 0:
            bl[i] = 0
        else:
            p = l1[i-1]
            bl[i] = p
    except:
        break



finalbl = ''.join(map(str, bl))
anglevalue = int(finalbl,2)
print(anglevalue)




