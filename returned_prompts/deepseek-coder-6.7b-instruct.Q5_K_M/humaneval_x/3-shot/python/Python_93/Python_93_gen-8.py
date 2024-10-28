    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    trans = str.maketrans(alphabet, alphabet[26:] + alphabet[:26])
    return ''.join(c.translate(trans) if c not in vowels else alphabet[alphabet.index(c)+2] for c in message)


