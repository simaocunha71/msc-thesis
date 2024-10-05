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
The `encode_shift` function works by iterating over each character in the input string, shifting its ASCII value by 5 places in the alphabet, and then converting it back to a character. The `decode_shift` function does the reverse operation, subtracting 5 from the ASCII value of each character before converting it back to a character. Both functions use list comprehension to process the input string character by character, and the `join` method to concatenate the resulting characters into a single string.