
def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in s:
        if char in alphabet:
            encrypted += alphabet[alphabet.index(char) + 2*2]
        else:
            encrypted += char
    return encrypted
