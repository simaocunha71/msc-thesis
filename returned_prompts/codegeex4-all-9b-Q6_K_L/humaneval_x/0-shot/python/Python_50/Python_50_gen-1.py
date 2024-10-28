
```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# Test the functions
encoded = encode_shift("hello")
decoded = decode_shift(encoded)

encoded, decoded
```

```result
('mjqqt', 'hello')
```

The `encode_shift` function has encoded the string "hello" to "mjqqt". The `decode_shift` function has successfully decoded it back to "hello".
