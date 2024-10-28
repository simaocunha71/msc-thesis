    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        if char.isalpha():
            if char.islower():
                index = (alphabet.index(char) + 4) % 26
                encrypted += alphabet[index]
            else:
                index = (alphabet.index(char.lower()) + 4) % 26
                encrypted += alphabet[index].upper()
        else:
            encrypted += char

    return encrypted


