
Here's a Python function that takes in a string and returns a new string with every character shifted by 5 in the alphabet:

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
```

This function works by using the `ord()` function to get the Unicode value of each character in the input string. It then adds 5 to the Unicode value, subtracts the Unicode value of 'a' (to keep the character within the range of lowercase alphabetical characters), takes the modulus of 26 (to wrap around the alphabet if the result exceeds 'z'), and finally adds the Unicode value of 'a' again to get the new Unicode value of the shifted character. The `chr()` function is then used to convert the new Unicode value back into a character, and all the characters are joined together into a new string using the `join()` function.

Here's a Python function that takes in a string encoded with the `encode_shift` function and returns the decoded string:

```python
def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 + ord("a")) % 26) + ord("a")) for ch in s])
```

This function works in a similar way to the `encode_shift` function, but instead of adding 5 to the Unicode value, it subtracts 5. This undoes the shift of 5 characters in the alphabet that was applied in the `encode_shift` function.

To use these functions, you can simply call them with a string as the argument. For example, to encode the string "hello" with a shift of 5, you would call `encode_shift("hello")`, which would return the string "mjqqt". To decode this string back to "hello", you would call `decode_shift("mjqqt")`, which would return the