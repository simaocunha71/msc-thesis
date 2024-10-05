```
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + 4) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result
```