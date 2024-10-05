```
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])
```


Explanation:
- We use the built-in `ord` function to get the ASCII value of a character.
- For lowercase letters, we shift the ASCII value by 5 and take the modulus of 26 to wrap around the alphabet.
- For uppercase letters, we need to adjust the shift accordingly. We can use the same logic, but we need to adjust the ASCII values and the modulus.
- For non-alphabetic characters, we just return the original character.
- The decode_shift function does the opposite, it subtracts 5 from the ASCII value and takes the modulus of 26 to shift the characters back to their original position. 

Note: The `isalpha` function is used to check if a character is a letter (either uppercase or lowercase). This helps to preserve non-alphabetic characters in the input string. 

Also, the `chr` function is used to convert the ASCII value back to a character. This is the reverse operation of the `ord` function. 





Final Answer: The final answer is the provided code. I hope it is correct.