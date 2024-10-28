def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_char = alphabet[(index + 4) % 26]
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string

print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'