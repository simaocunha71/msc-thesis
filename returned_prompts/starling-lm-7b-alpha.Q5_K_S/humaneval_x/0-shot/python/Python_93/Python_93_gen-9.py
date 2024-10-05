
def encode(message):
    vowels = "AEIOU"
    result = ""
    for c in message:
        if c in vowels:
            result += chr(ord(c) + 1)
        elif c.isupper():
            result += chr(ord(c) + 32)
        elif c.islower():
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

# Tests
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'





def encode(message):
    result = ""
    vowels = "AEIOU"
    for c in message:
        if c in vowels:
            result += chr(ord(c) + 1)
        else:
            if c.isupper():
                result += chr(ord(c) + 32)
            else:
                result += chr(ord(c) - 32)
    return result

# Tests
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'





def encode(message):
    vowels = "AEIOU"
    result = ""
    for c in message:
        if c in vowels:
            result += chr(ord(c) + 1)
        else:
            if c.isupper():
                result += chr(ord(c) + 32)
            else:
                result += chr(ord(c) - 32)
    return result

# Tests
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'





def encode(message):
    vowels = "AEIOU"
    result = ""
    for c in message:
        if c in vowels:
            result += chr(ord(c) +