
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2
    encoded = ''
    for char in message:
        if char in alphabet:
            if char.islower():
                encoded += alphabet[alphabet.index(char) + shift].upper()
            else:
                encoded += alphabet[alphabet.index(char) + shift]
        else:
            encoded += char
    return encoded
