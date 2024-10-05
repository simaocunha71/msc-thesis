

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Testing
s = "hello"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Original: {s}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")


Output:

Original: hello
Encoded: mjqqt
Decoded: hello

The encode_shift function works by shifting each character 5 positions to the right in the alphabet, wrapping around when reaching the end of the alphabet. The decode_shift function does the opposite by shifting 5 positions to the left. This creates a basic Caesar cipher, a type of substitution cipher where each character in the plaintext is shifted a certain number of places down the alphabet.

The encoding and decoding is done by manipulating the ASCII values of the characters. The ord function is used to get the ASCII value of a character, and the chr function is used to convert an ASCII value back to a character. The modulo operator (%) is used to wrap the value around when reaching the end of the alphabet.

The function works for lowercase English letters only. If you want to use it for other characters or languages, you would need to modify the function to handle those cases.

Note: This is a very simple form of cipher and it is not secure for most purposes. It's used here just to demonstrate the concept of encoding and decoding.
"""

