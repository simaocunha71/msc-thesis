```python
def encrypt(s):
    return ''.join([chr((ord(c) - 97 + 4) % 26 + 97) for c in s])
```
