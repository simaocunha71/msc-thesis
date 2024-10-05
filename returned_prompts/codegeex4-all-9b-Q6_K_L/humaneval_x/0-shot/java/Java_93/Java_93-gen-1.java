def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isupper():
            if char in vowels:
                encoded_message += chr(ord(char) + 2).upper()
            else:
                encoded_message += char.lower()
        else:
            if char in vowels:
                encoded_message += chr(ord(char) + 2).lower()
            else:
                encoded_message += char.upper()
    return encoded_message

# Test cases
print(encode("test")) # "TGST"
print(encode("This is a message")) # "tHKS KS C MGSSCGG"