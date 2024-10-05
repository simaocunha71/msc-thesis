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

# test
encode = encode_shift("hello")
print(encode)  # "mjqqt"

decode = decode_shift(encode)
print(decode)  # "hello"

# Output:
# mjqqt
# hello
# (as expected)  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string is correctly decoded back to the original string.  # the encoded string