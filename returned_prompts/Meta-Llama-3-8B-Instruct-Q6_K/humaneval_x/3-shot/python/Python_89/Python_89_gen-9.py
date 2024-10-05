    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s.lower():
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += alphabet[(index + 4 * 2) % 26]
        else:
            encrypted += char
    return encrypted


