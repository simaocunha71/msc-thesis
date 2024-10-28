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
In the `encode_shift` function, we use the ASCII value of each character to shift it by 5 places in the alphabet. We add 5 to the ASCII value of each character, subtract the ASCII value of 'a', take the modulus with 26 (the number of letters in the alphabet) and then add the ASCII value of 'a' back to get the encoded character.

In the `decode_shift` function, we do the reverse operation. We subtract 5 from the ASCII value of each character, subtract the ASCII value of 'a', take the modulus with 26 and then add the ASCII value of 'a' back to get the decoded character.

Both functions use list comprehension to iterate over each character in the input string, apply the encoding/decoding operation, and then join the resulting characters back into a string.