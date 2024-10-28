
def encode(message):
    # make a list of all the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # make an empty list to store the encoded message
    encoded_message = []
    # go through each character in the message
    for letter in message:
        # if the letter is a vowel
        if letter in vowels:
            # replace it with the letter that is 2 places ahead of it
            encoded_message.append(vowels[(vowels.index(letter) + 2) % 5])
        # otherwise
        else:
            # just add the original letter to the encoded message
            encoded_message.append(letter)
    # return the encoded message
    return ''.join(encoded_message)
