
def encode(message):
    vowel = "aeiou"
    message = message.lower()
    res = ""
    for i in message:
        if i in vowel:
            if i == "a":
                res += "c"
            elif i == "e":
                res += "g"
            elif i == "i":
                res += "k"
            elif i == "o":
                res += "q"
            else:
                res += "s"
        else:
            if i.islower():
                res += chr(ord(i) - 32)
            else:
                res += chr(ord(i) + 32)
    return res

# Test
print(encode('test')) # 'TGST'
print(encode('This is a message')) # 'tHKS KS C MGSSCGG'


# Other solution
def encode(message):
    vowel = "aeiou"
    res = ""
    for i in message:
        if i in vowel:
            res += vowel[(vowel.index(i) + 2) % 5]
        else:
            if i.islower():
                res += i.upper()
            else:
                res += i.lower()
    return res

# Test
print(encode('test')) # 'TGST'
print(encode('This is a message')) # 'tHKS KS C MGSSCGG'




# Other solution
def encode(message):
    vowel = "aeiou"
    res = ""
    for i in message:
        if i in vowel:
            res += vowel[(vowel.index(i) + 2) % 5]
        else:
            if i.islower():
                res += i.upper()
            else:
                res += i.lower()
    return res

# Test
print(encode('test')) # 'TGST'
print(encode('This is a message')) # 'tHKS KS C MGSSCGG'
