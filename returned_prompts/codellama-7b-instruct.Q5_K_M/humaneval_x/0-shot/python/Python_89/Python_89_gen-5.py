
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2
    encrypted = ''
    for i in s:
        if i in alphabet:
            encrypted += alphabet[(alphabet.index(i) + shift) % 26]
        else:
            encrypted += i
    return encrypted
