    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2 * 2:] + alphabet[:2 * 2]
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                index = alphabet.index(char)
                encrypted_string += rotated_alphabet[index]
            else:
                index = alphabet.index(char.lower())
                encrypted_string += rotated_alphabet[index].upper()
        else:
            encrypted_string += char
    return encrypted_string


