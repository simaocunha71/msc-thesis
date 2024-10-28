def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_alphabet = alphabet[2:] + alphabet[:2]
    encrypted_string = ''
    for c in s:
        if c in alphabet:
            encrypted_string += encrypted_alphabet[alphabet.index(c)]
        else:
            encrypted_string += c
    return encrypted_string

print(encrypt('hi')) # 'lm'
print(encrypt('asdfghjkl')) # 'ewhjklnop'
print(encrypt('gf')) # 'kj'
print(encrypt('et')) # 'ix'