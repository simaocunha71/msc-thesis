

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# test the functions
s = "hello"
encoded_s = encode_shift(s)
decoded_s = decode_shift(encoded_s)

print("Original string: ", s)
print("Encoded string: ", encoded_s)
print("Decoded string: ", decoded_s)
<jupyter_output>
Original string:  hello
Encoded string:  mjqqt
Decoded string:  hello
<jupyter_text>
Problem 2: Caesar Cipher (Shift) (40 points)In the previous problem, you implemented a Caesar Cipher for English alphabet. Now, implement the Caesar Cipher for a general alphabet (doesn't have to be English).
<jupyter_code>
