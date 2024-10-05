    def encrypt(s):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_alphabet = alphabet[2:] + alphabet[:2]
        new_alphabet += alphabet[2:] + alphabet[:2]
        return ''.join([new_alphabet[alphabet.index(c)] if c in alphabet else c for c in s])


