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


Here's a brief explanation:

*   The `encode_shift` function takes a string `s` as input and returns an encoded string.
*   It does this by iterating over each character `ch` in the input string.
*   For each character, it calculates the ASCII value of the character shifted 5 positions forward in the alphabet.
*   This is done using the formula `((ord(ch) + 5 - ord("a")) % 26) + ord("a")`, which ensures that the shift wraps around the alphabet correctly.
*   The resulting ASCII values are then converted back to characters using the `chr` function, and these characters are concatenated together to form the encoded string.
*   The `decode_shift` function is the inverse of `encode_shift`. It takes an encoded string as input and returns the original string.
*   It does this by iterating over each character `ch` in the input string and calculating the ASCII value of the character shifted 5 positions backward in the alphabet.
*   This is done using the formula `((ord(ch) - 5 - ord("a")) % 26) + ord("a")`, which is the inverse of the formula used in `encode_shift`.
*   The resulting ASCII values are then converted back to characters using the `chr` function, and these characters are concatenated together to form the decoded string.