```python

def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = index + 8
            if new_index >= len(alphabet):
                new_index -= len(alphabet)
            if char.isupper():
                encrypted += alphabet[new_index].upper()
            else:
                encrypted += alphabet[new_index]
        else:
            encrypted += char
    return encrypted

```
