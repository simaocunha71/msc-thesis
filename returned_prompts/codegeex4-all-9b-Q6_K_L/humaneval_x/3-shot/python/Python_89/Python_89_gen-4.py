    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in s:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + 4) % 26
            result += alphabet[index].upper() if char.isupper() else alphabet[index]
        else:
            result += char
    return result

