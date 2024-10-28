
def encode(message):
    vowels = 'aeiou'
    result = ""
    for c in message:
        if c.lower() in vowels:
            c = chr((ord(c) + 2) % 26 + ord('a'))
        elif c.isupper():
            c = chr((ord(c) + 2) % 26 + ord('A'))
        elif c.islower():
            c = chr((ord(c) + 2) % 26 + ord('a'))
        result += c
    return result

# Alternative solution:
from string import ascii_lowercase, ascii_uppercase
from itertools import chain

def encode(message):
    vowels = chain(ascii_lowercase, ascii_uppercase)[5:9]
    result = ""
    for c in message:
        if c in vowels:
            c = chr((ord(c) + 2) % 26 + ord(c))
        result += c
    return result

# Testing:
print(encode('test')) # 'TGST'
print(encode('This is a message')) # 'tHKS KS C MGSSCGG'

# From:
# https://stackoverflow.com/questions/9060302/python-itertools-chain-example
```
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
