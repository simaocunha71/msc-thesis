def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for c in s:
        if c in alphabet:
            index = alphabet.index(c)
            new_index = (index + 4) % 26
            encrypted += alphabet[new_index]
        else:
            encrypted += c
    return encrypted

print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'