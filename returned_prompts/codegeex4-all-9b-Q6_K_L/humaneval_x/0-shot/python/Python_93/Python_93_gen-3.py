def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += chr(ord(char) + 2)
        elif char.isalpha():
            encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message

print(encode('test'))
print(encode('This is a message'))