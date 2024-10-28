    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            if char.islower():
                index = alphabet.index(char)
                encrypted += alphabet[(index + shift) % 26]
            else:
                index = alphabet.index(char.lower())
                encrypted += alphabet[(index + shift) % 26].upper()
        else:
            encrypted += char
    return encrypted


