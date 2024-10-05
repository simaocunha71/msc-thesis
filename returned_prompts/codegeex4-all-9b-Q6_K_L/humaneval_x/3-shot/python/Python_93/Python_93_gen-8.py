    vowels = 'aeiou'
    encoded_message = ''

    for c in message:
        if c.lower() in vowels:
            encoded_message += chr(ord(c) + 2)
        else:
            encoded_message += c.swapcase()

    return encoded_message

