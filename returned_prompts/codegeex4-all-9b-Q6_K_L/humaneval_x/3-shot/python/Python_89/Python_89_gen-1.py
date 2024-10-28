    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for c in s:
        if c.lower() in alphabet:
            index = alphabet.index(c.lower())
            encrypted += alphabet[(index + 4) % 26]
        else:
            encrypted += c

    return encrypted

