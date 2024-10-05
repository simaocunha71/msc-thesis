def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            if char.islower():
                encoded_message += chr(ord(char) + 2).upper()
            else:
                encoded_message += chr(ord(char) + 2).lower()
        else:
            encoded_message += char.swapcase()
    return encoded_message

print(encode('test'))
print(encode('This is a message'))