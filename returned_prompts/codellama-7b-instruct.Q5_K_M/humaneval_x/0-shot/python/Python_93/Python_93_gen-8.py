
def encode(message):
    vowels = 'aeiou'
    message = message.swapcase()
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + vowels[vowels.index(message[i]) + 2] + message[i+1:]
    return message
