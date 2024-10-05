
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[2:] + alphabet[:2]
    result = ''
    for c in s:
        result += new_alphabet[alphabet.index(c)]
    return result