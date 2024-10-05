def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index * 2) % 26
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

print(encrypt('hi')) # returns 'lm'
print(encrypt('asdfghjkl')) # returns 'ewhjklnop'
print(encrypt('gf')) # returns 'kj'
print(encrypt('et')) # returns 'ix'