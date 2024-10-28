    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char in alphabet:
            index = (alphabet.index(char) + 4) % 26
            encrypted += alphabet[index]
        else:
            encrypted += char
    return encrypted

