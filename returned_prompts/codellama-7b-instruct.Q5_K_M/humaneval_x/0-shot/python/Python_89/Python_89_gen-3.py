
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[2:] + alphabet[:2]
    return ''.join(alphabet[alphabet.index(c)] for c in s)
