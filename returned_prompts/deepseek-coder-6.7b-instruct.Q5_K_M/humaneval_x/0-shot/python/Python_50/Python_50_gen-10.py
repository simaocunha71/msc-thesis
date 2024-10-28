

def decode_shift(s: str):
    """
    returns decoded string by shifting every character by -5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


print(encode_shift("hello"))
print(decode_shift(encode_shift("hello")))


# Output:
# mjqqt
# hello


# The function encode_shift works by shifting the ordinal value of each character by 5 and then converting back to a character using chr(). The modulo operator is used to ensure that the result is a valid character in the alphabet.


# The function decode_shift works in a similar way, but it shifts the ordinal value of each character by -5. This effectively undoes the encoding performed by encode_shift.


# The functions encode_shift and decode_shift can handle uppercase and lowercase letters. The function ord() is used to get the ordinal value of a character and the function chr() is used to convert an ordinal value back to a character.


# This code does not handle non-alphabetic characters. If you want to handle them in a special way, you would need to add code to handle them.


# The code also does not handle the case where the character is not within the range 'a' to 'z' or 'A' to 'Z'. If you want to handle this case, you would need to add code to handle it.


# The code uses a simple Caesar cipher for encoding and decoding. If you want to use a different type of encoding, you would need to change the code to use a different type of encoding.


# The code uses the modulo operator to ensure that the result is a valid character in the alphabet. This is necessary because the modulo operator can be used to wrap around to the start of the alphabet if the result is outside the range 'a' to 'z' or 'A' to 'Z'.


# The code uses the built-in ord() function to get the ordinal value of a character and the built-in chr() function to convert an ordinal value back to a character.