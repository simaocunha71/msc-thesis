    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''

    for char in s:
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            encrypted_char_index = (char_index + 4) % 26
            encrypted_char = alphabet[encrypted_char_index]

            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_string += encrypted_char
        else:
            encrypted_string += char

    return encrypted_string


