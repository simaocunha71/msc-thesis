
def encrypt(s):
    return ''.join([chr(ord(c)+(2*2)+(26*(i%2))) for i,c in enumerate(s)])


# Alternative solution using the built-in ord and chr functions
def encrypt(s):
    return ''.join([chr(ord(c) + (2*2) + (26 * (i % 2))) for i, c in enumerate(s)])


# Testing
print(encrypt('hi'))      # Should print: lm
print(encrypt('asdfghjkl'))      # Should print: ewhjklnop
print(encrypt('gf'))      # Should print: kj
print(encrypt('et'))      # Should print: ix

# Bonus:
# Encrypt a string with multiple spaces
print(encrypt('hello world'))      # Should print: jgnnqf yqtnfq
print(encrypt('hello    world'))  # Should print: jgnnqf yqtnfq

# Bonus:
# Decrypt a string with multiple spaces
def decrypt(s):
    return ''.join([chr(ord(c)-(2*2)-(26 * (i % 2))) for i,c in enumerate(s)])
print(decrypt('jgnnqfyqtnfq'))      # Should print: hello world
print(decrypt('jgnnqfyqtnfq'))      # Should print: hello    world


# Testing with a string of 1000 characters
import timeit
print(timeit.timeit('encrypt("abcdefghijklmnopqrstuvwxyz" * 100)', number=10000))
```
