    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + 4) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text

