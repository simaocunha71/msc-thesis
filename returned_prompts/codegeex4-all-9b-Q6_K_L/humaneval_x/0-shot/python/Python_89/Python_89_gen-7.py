def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''
    for char in s:
        if char.lower() in alphabet:
            if char.isupper():
                encrypted_string += alphabet.upper()[alphabet.index(char.lower()) + 4].upper()
            else:
                encrypted_string += alphabet[alphabet.index(char.lower()) + 4]
        else:
            encrypted_string += char
    return encrypted_string

print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))