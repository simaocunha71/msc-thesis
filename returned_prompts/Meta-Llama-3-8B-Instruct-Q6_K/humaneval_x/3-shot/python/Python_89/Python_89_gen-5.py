    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            index = alphabet.index(char.lower())
            new_index = (index + shift) % len(alphabet)
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char
    return result


