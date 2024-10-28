    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2
    encrypted = ''
    for char in s:
        if char.isalpha():
            index = alphabet.index(char.lower())
            new_index = (index + shift) % 26
            if char.isupper():
                encrypted += alphabet[new_index].upper()
            else:
                encrypted += alphabet[new_index]
        else:
            encrypted += char
    return encrypted


