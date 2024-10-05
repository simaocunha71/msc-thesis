    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_alphabet = alphabet[2:] + alphabet[:2]
    encrypted_string = ''

    for c in s:
        if c in alphabet:
            index = alphabet.index(c)
            encrypted_string += encrypted_alphabet[index]
        else:
            encrypted_string += c

    return encrypted_string

