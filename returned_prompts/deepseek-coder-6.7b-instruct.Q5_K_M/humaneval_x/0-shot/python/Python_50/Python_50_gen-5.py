

def decode_shift(s: str):
    """
    returns decoded string by shifting every character 5 positions to the left in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Test Cases:

print(encode_shift("hello"))  # Output: 'mjqqt'
print(decode_shift("mjqqt"))  # Output: 'hello'
print(encode_shift("world"))  # Output: 'btwqi'
print(decode_shift("btwqi"))  # Output: 'world'


# The encode_shift function works by using the ord function to get the ASCII value of each character in the string, 
# then adding 5 to that value and taking the modulo 26 of the result to ensure that the new value is still within the 
# ASCII values of the alphabet characters. Then the chr function is used to convert the new ASCII value back to a 
# character. This is repeated for every character in the string to get the encoded string.

# The decode_shift function works in a similar way, but instead of adding 5 to the ASCII value, it subtracts 5. 
# This is because the encoding process moves each character 5 positions to the right in the alphabet.

# These functions are case-sensitive and only work with lowercase letters. They do not handle non-alphabetic characters 
# or uppercase letters.

# This is a basic form of a Caesar cipher, which is a type of substitution cipher where each character in the plaintext 
# is 'shifted' a certain number of places down or to the right the alphabet. In this case, the shift is 5 places.


# Note: The ord function returns the ASCII value of a character and the chr function returns the character 
# represented by a specific ASCII value.

# The modulo operation (% 26) is used to ensure that the new ASCII value is still within the range of ASCII 
# values of the alphabet characters. This is because the ASCII values of the