
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2
    encrypted = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + shift
            if new_index > 25:
                new_index = new_index - 26
            encrypted += alphabet[new_index]
        else:
            encrypted += char
    return encrypted

