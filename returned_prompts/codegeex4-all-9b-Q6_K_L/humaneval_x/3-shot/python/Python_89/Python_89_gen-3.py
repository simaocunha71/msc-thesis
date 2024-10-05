    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index + 4) % 26
            encrypted += alphabet[new_index].upper() if char.isupper() else alphabet[new_index]
        else:
            encrypted += char

    return encrypted

