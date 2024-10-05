    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''

    for char in s:
        if char.isalpha():
            if char.islower():
                index = (alphabet.index(char) + 8) % 26
                encrypted_string += alphabet[index]
            else:
                index = (alphabet.index(char.lower()) + 8) % 26
                encrypted_string += alphabet[index].upper()
        else:
            encrypted_string += char

    return encrypted_string


