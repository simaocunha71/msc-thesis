
def encode(message):
    # Create a dictionary with the vowels and their corresponding 
    # shifted positions in the alphabet.
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 'q'}

    # Create a list of characters for the encoded message.
    encoded_message = []

    # Loop through each character in the message.
    for character in message:
        # If the character is a vowel, add the corresponding shifted 
        # character to the encoded message.
        if character in vowels:
            encoded_message.append(vowels[character])
        else:
            # Otherwise, add the character itself to the encoded message.
            encoded_message.append(character)

    # Return the encoded message as a string.
    return ''.join(encoded_message)

def test():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('abcdefghijklmnopqrstuvwxyz') == 'cdefghijklmnopqrstuvwxyza'
    assert encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'CDEFGHIJKLMNOPQRSTUVWXYZA'
    print('All tests passed!')

test()