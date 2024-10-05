```
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
```

Explanation:

The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet. It does this by subtracting the ASCII value of 'a' from the ASCII value of each character, adding 5, and then taking the remainder when divided by 26 (the number of letters in the alphabet). The result is the ASCII value of the encoded character, which is converted back to a character using the `chr` function.

The `decode_shift` function does the reverse: it shifts every character in the input string back by 5 positions in the alphabet. It does this by subtracting 5 from the ASCII value of each character, subtracting the ASCII value of 'a', and then taking the remainder when divided by 26. The result is the ASCII value of the decoded character, which is converted back to a character using the `chr` function. This is the inverse operation of the `encode_shift` function.