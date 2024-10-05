
def encode(message):
    # replace vowels with 2 letters ahead
    # swap case
    # return the encoded message
    vowels = 'aeiou'
    encoded = ''
    for i in message:
        if i in vowels:
            encoded += chr(ord('a') + (ord(i) - ord('a') + 2) % 26)
        else:
            encoded += chr(ord('A') + (ord(i) - ord('A') + 2) % 26)
    return encoded

    # another way
    encoded = ''.join([chr(ord(i) + (ord(i) - ord('a') + 2) % 26) for i in message])
    return encoded.swapcase()
