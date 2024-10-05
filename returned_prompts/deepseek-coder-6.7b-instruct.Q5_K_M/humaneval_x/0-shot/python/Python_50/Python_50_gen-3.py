

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# testing
s = "hello"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Original: {s}, Encoded: {encoded}, Decoded: {decoded}")

s = "world"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Original: {s}, Encoded: {encoded}, Decoded: {decoded}")


This will work for lowercase alphabetical characters only. If you also want to encode uppercase letters, you can add another set of 26 letters to the mix with their corresponding shift.
"""

# solution
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord('a') + 5) % 26) + ord('a')) if 'a' <= ch <= 'z' else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord('a') - 5) % 26) + ord('a')) if 'a' <= ch <= 'z' else ch for ch in s])


# testing
s = "hello"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Original: {s}, Encoded: {encoded}, Decoded: {decoded}")

s = "world"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Original: {s}, Encoded: {encoded}, Decoded