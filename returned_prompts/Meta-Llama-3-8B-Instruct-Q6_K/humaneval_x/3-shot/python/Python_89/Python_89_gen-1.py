    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2*2:] + alphabet[:2*2]
    result = ''
    for char in s:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if char.isupper():
                result += rotated_alphabet[index].upper()
            else:
                result += rotated_alphabet[index]
        else:
            result += char
    return result


