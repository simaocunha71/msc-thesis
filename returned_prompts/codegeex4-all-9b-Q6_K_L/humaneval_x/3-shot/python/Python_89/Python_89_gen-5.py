    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in s:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            encrypted_index = (index + 4) % 26
            encrypted_char = alphabet[encrypted_index]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

