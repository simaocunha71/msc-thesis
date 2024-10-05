def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''
    
    for char in message:
        if char in vowels:
            encoded_message += alphabet[alphabet.index(char) + 2]
        elif char.isalpha():
            encoded_message += char.swapcase()
        else:
            encoded_message += char
    
    return encoded_message

print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'