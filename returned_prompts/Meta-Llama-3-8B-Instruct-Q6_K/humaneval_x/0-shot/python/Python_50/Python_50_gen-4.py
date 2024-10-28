```
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])
```


Explanation:
1.  `encode_shift` function shifts every character in the input string `s` by 5 positions in the alphabet. It works by subtracting the ASCII value of 'a' from the ASCII value of the character, adding 5, and then taking the modulus 26 to wrap around the alphabet. The result is then converted back to a character using `chr`.
2.  `decode_shift` function is the inverse of `encode_shift`. It shifts every character in the input string `s` by 5 positions in the opposite direction (i.e., towards the beginning of the alphabet). It does this by subtracting 5 from the result of the `encode_shift` operation, effectively reversing the shift.
3.  The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to convert an ASCII value back to a character.
4.  The `% 26` operation is used to wrap around the alphabet when the shift goes beyond 'z' or 'Z'. This ensures that the function works correctly even when the input string contains characters that are shifted past the end of the alphabet.